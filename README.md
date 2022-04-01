# ctfd-q-ripper
grabs all ctfd questions from host via api for offline use

## usage
```
usage: ctfd-q-ripper.py [-h] --path PATH --url URL --cookie COOKIE

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      output directory
  --url URL        base ctfd url
  --cookie COOKIE  copy+paste http cookie from authenticated session
```

### usage example
```
python3 ctfd-q-ripper.py \
  --path "demo" \
  --url "https://demo.ctfd.io/" \
  --cookie "session=b9e94c6f-5cd8-4da7-accd-2e0130923722.tWFmIajAUAkmzk8i9DJiMJFzgt8"
```

## output example
`cat 'demo/Multiple Choice/Trivia/prompt.txt'`
```
What is the answer to life, the universe, and everything?

* () The Cake
* () 42
* () The Red Umbrella
* () All of the above
-----------------------------

Points: 42
```
