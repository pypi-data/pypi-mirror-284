# ttshandler
A Python library that provides a simple and intuitive API for seamless interfacing with text-to-speech libraries like **gtts** and **pyttsx3**.

## Features
* Combines the full potential of two popular Test-to-Speech libraries: **gtts** and **pyttsx3** into a single one.
* Strict enforcement of valid values for setting the speech properties supported by the respective APIs.
* Generate an audio output file for the text-to-speech.
* Generate a visual waveform of the text-to-speech audio.

## Dependencies
Most dependencies will be automatically installed if you install ttshandler from pip using the command:    
```pip3 install ttshandler```.

Dependencies include:
* ```pyttsx3```
* ```gtts```
* ```matplotlib```
* ```numpy```
* ```pydub```

Additionally, you also need ```ffmpeg``` pre-installed on your system. While ```ffmpeg``` is not directly
required for ttshandler, it is a basic requirement for ```pydub``` to work.   

Install ```ffmpeg``` using your package manager:
* On Debian/Ubuntu based systems with ```apt``` use the command: ```sudo apt install ffmpeg```
* For Arch Linux/systems with ```pacman``` use: ```sudo pacman -S ffmpeg```
* For other systems, get it from [here](https://www.ffmpeg.org/download.html).

After installing, add ```ffmpeg``` to the system's PATH variable. This process is not required if you
installed ```ffmpeg``` using your package manager.    


## Version Requirements
### Executables
* Python >= 3.8
* ```ffmpeg``` (latest version recommended)
### Python libraries
* ```gtts``` >= 2.5.1
* ```pyttsx3``` >= 2.90
* ```matplotlib``` >= 3.6.0
* ```numpy``` >= 1.24.0
* ```pydub``` >= 0.25.1

## Example code snippets
After installing ttshandler, you may run the following example code snippets:
### Example using pyttsx3
```
>>> import ttshandler as ttsh
>>> tts = ttsh.TTSHandler(text="Hello world", api="pyttsx3")
>>> tts.generate_tts("tts_pyttsx3.wav")
>>> tts.generate_waveform("waveform_pyttsx3.png")
```
If no errors are generated, you will have two files in your current working directory that contain
the text-to-speech audio clip generated using ```pyttsx3``` and the audio waveform image, respectively.

### Example using gtts
```
>>> import ttshandler as ttsh
>>> tts2 = ttsh.TTSHandler(text="Hello world", api="gtts")    # Requires internet connection
>>> tts2.generate_tts("tts_gtts.mp3")
>>> tts2.generate_waveform("waveform_gtts.png")
```
```gtts``` requires internet connection. ttshandler will raise a ```GTTSConnectonError``` if ```gtts``` fails to connect to Google's text-to-speech API.


# Detailed documentation

## Directory structure of package ```ttshandler```
```
ttshandler/
    |
    |____    __init__.py
    |____    ttsexceptions.py
    |____    ttshandler.py
```

## Module ```__init__.py```
Imports the main module ```ttshandler.py```.

## Module ```ttsexceptions.py```
Exception that are raised from the TTSHandler class are defined here. These are:

```class UnknownAPIError(Exception)```
* Raised when the API specified while initializing TTSHandler is not one of 'pyttsx3' or 'gtts'.

```class TTSPropertyError(Exception)```
* Raised while attempting to set an invalid or unsupported property for an initialized API.

```class TTSNotGeneratedError(Exception)```
* Raised when attempting to generate a speech waveform before the TTS has been generated.

```class GTTSConnectionError(Exception)```
* Raised when ```gtts.tts.gTTSError``` is raised, which occurs mainly due to connection issues.

```class Pyttsx3InitializationError(Exception)```
* Raised when Pyttsx3 could not initialize the specified TTS engine.

```class NoFFmpegError(Exception)```
* Raised when FFmpeg is not installed, which is required for audio format conversions.

## Module ```ttshandler.py```
This is the main module containing the TTSHandler class.

```class TTSHandler```    
Functions defined here:

* ```def __init__(self, text, api, pyttsx3engine='default')```  
    Initialize the TTSHandler class. ```-api``` must be either ```'pyttsx3'``` or ```'gtts'``` (only these are supported). ```-text``` should be a string which will be converted into speech. An optional keyword argument ```-pyttsx3engine``` may be specified in case a non-default TTS engine is desired to be used. This option is ignored if ```api='gtts'```.

* ```def set_property(self, **properties)```    
    Set the speech properties. Pyttsx3 supported options are ```-rate```, ```-volume``` and ```-voice```.
  * ```-rate``` : an integer from 50 to 300 denoting the number of words per minute (default=```150```);
  * ```-volume``` : a float value from 0.0 to 1.0 that sets the volume of the speech (default=```1.0```);
  * ```-voice``` : an integer denoting the index of the voice as returned by ```engine.getProperty('voices')``` (default=```0``` [the first voice]).    

  GTTS supported options are ```-tld```, ```-lang``` and ```-slow```.
  * ```-tld``` : set the top-level domain used by GTTS for non-local accents (default=```'com'``` [local accent]);
  * ```-lang``` : set the language for TTS (default=```'en'```). Both IETF language tags and language names are supported, but to avoid case-sensitivity issues use the IETF tags.
  * ```-slow``` : boolean to set whether the speech will be normal or slowed (default=```False```).    
  
  For more details, refer to the respective documentations of [Pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) or [GTTS](https://gtts.readthedocs.io/en/latest/).

* ```def generate_tts(self, output_file='')```    
    Generate the TTS output. ```-output_file``` accepts an absolute path for saving the TTS. If ```-output_file``` is not specified, TTS is generated in the system's temp directory. Currently for ```api='pyttsx3'``` only .wav files are generated and for ```api='gtts'``` only .mp3 files are generated. If the output filename does not end with either of these, (case-insensitive) the respective file extensions are appended to the output filename (.wav for pyttsx3 and .mp3 for gtts). This behaviour may be updated in the future for support of multiple audio file types.

* ```def generate_waveform(self, output_file, **kwargs)```    
    Generate a pictorial wave form of the TTS audio. ```-output_file``` accepts an absolute file path for saving the waveform as a PNG file. If the file has extension other than .png (case-insensitive), .png would be appended to the file and saved as PNG.
    Accepted keyword arguments are:
  * ```-dimensions``` : a string in the form of ```"<width>x<length>"``` specifying the dimensions of the output image (default="800x600");
  * ```-fgcolor``` : a color in RGBA format (eg: ```'#060e32'```) or any other valid color name that is recognized by ```matplotlib.pyplot``` (default=```'skyblue'```);
  * ```-bgcolor``` : same as ```-fgcolor``` (default=```'white'```).    
  
  This function will raise a ```TTSNotGeneratedError``` if it is executed before running ```generate_tts()```.


# TODO
* Add support for saving TTS audio clips in various other file types besides .mp3 and .wav.


# License
ttshandler is available under the MIT License.
