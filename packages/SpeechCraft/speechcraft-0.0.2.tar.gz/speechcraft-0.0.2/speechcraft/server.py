import argparse

try:
    import fastapi
    from fast_task_api import FastTaskAPI, JobProgress, AudioFile, MediaFile
except ImportError:
    raise ImportError("Please install the full version of speechcraft with pip install speechcraft[server]"
                      " to use the server functionality.")

import speechcraft as t2v
from speechcraft.supp.model_downloader import download_all_models_init
from speechcraft.settings import DEFAULT_PORT, PROVIDER

import os

from speechcraft.supp.utils import encode_path_safe

app = FastTaskAPI(
    provider=PROVIDER,
    app=fastapi.FastAPI(
        title="SpeechCraft by SocAIty.",
        summary="Create audio from text, clone voices and use them. Convert voice2voice. "
                "Generative text-to-audio Bark model.",
        version="0.0.1",
        contact={
            "name": "SocAIty",
            "url": "https://github.com/SocAIty/text2speech",
        })
)

@app.task_endpoint(path="/text2voice", queue_size=10)
def text2voice(
        job: JobProgress,
        text: str,
        voice: str = "en_speaker_3",
        semantic_temp: float = 0.7,
        semantic_top_k: int = 50,
        semantic_top_p: float =0.95,
        coarse_temp: float = 0.7,
        coarse_top_k: int = 50,
        coarse_top_p: float =0.95,
        fine_temp: float = 0.5
    ):
    """
    :param text: the text to be converted
    :param voice: the name of the voice to be used. Uses the pretrained voices which are stored in models/speakers folder.
        It is also possible to provide a full path.
    :return: the audio file as bytes
    """

    # validate parameters
    # remove any illegal characters from text
    text = encode_path_safe(text)

    job.set_status(progress=0.2, message="Started text2voice.")

    generated_audio_file, sample_rate = t2v.text2voice(
        text=text,
        voice=voice,
        semantic_temp=semantic_temp,
        semantic_top_k=semantic_top_k,
        semantic_top_p=semantic_top_p,
        coarse_temp=coarse_temp,
        coarse_top_k=coarse_top_k,
        coarse_top_p=coarse_top_p,
        fine_temp=fine_temp
    )

    # make a recognizable filename
    filename = text[:15] if len(text) > 15 else text
    filename = f"{filename}_{os.path.basename(voice)}.wav"
    af = AudioFile(file_name=filename).from_np_array(np_array=generated_audio_file, sr=sample_rate, file_type="wav")
    return af


@app.task_endpoint("/voice2embedding")
def voice2embedding(
        job: JobProgress,
        audio_file: AudioFile,
        voice_name: str = "new_speaker",
        save: bool = True
):
    """
    :param audio_file: the audio file as bytes 5-20s is good length
    :param voice_name: how the new voice / embedding is named
    :param save: if the embedding should be saved in the voice dir for reusage
    :return: the voice embedding as bytes
    """
    # create embedding vector
    bytesio = audio_file.to_bytes_io()
    job.set_status(progress=0.1, message=f"Started embedding creation {voice_name}.")
    embedding = t2v.voice2embedding(audio_file=bytesio, voice_name=voice_name)

    # write voice embedding to file
    if save:
        job.set_status(progress=0.98, message=f"Saving embedding {voice_name} to library.")
        embedding.save_to_speaker_lib()

    mf = MediaFile(file_name=f"{voice_name}.npz").from_bytesio(embedding.to_bytes_io(), copy=False)
    return mf


@app.task_endpoint("/voice2voice")
def voice2voice(
        job: JobProgress,
        audio_file: AudioFile,
        voice_name: str,
):
    """
    :param audio_file: the audio file as bytes 5-20s is good length
    :param voice_name: how the new voice / embedding is named
    :return: the converted audio file as bytes
    """

    # inference
    audio_array, sample_rate = t2v.voice2voice(audio_file.to_bytes_io(), voice_name)

    job.set_status(progress=0.1, message=f"Started voice2voice {voice_name}.")

    # convert to file
    af = AudioFile(file_name=f"voice2voice_{voice_name}.wav").from_np_array(
        np_array=audio_array,
        sr=sample_rate,
        file_type="wav"
    )

    return af


def start_server(port: int = DEFAULT_PORT):
    # first time load and install models
    download_all_models_init()
    app.start(port=port)


# start the server on provided port
if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    args = arg_parser.parse_args()
    start_server(port=args.port)
