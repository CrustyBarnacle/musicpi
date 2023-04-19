# musicpi
Control, status of Volumio music server over REST API

Point `VOLUMIO_HOST = "<volumio_hostname>"` to your [Volumio](https://volumio.com/en/get-started/) music server :-).

By Hostname (any hostname the system running this script can resolve):
  `VOLUMIO_HOST = musicpi.local`
  
Or, by IP address:
  `VOLUMIO_HOST = 1.2.3.4`

Volumio music server status, start, and stop playback.
Originally (still often used) a short zsh script with the
same functionality; This started from a [gist](https://gist.github.com/CrustyBarnacle/0f6b98d8fb5344f23330e54885a81a3a)!

## Running the script
To start the script (it will keep running until the user `(Q)uits`).
Example:
```shell
    $ python3 main.py
```
On GNU/Linux make the script executable, and run it directly.
In the repository directory:
```shell
    $ chmod u+x ./main.py
```
And then run directly:
```shell
    $ ./main.py
```
