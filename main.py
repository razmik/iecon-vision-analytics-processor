import importlib

video_analyzer = importlib.import_module('video_analyzer').getAnalyzer()

filename = 'C:/Users\pc\Downloads/videoplayback.mp4'.replace('\\', '/')
video_analyzer.start_capture(10, '52b05c830201461da09688253629ecd3', 'e9b3a0491efc46a8b29a3c48ab098f07', True, filename, False)
