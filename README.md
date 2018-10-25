Please run docker file using these command:

sudo docker build -t hotels .

sudo docker run  -v $(pwd):/app hotels

The output files will be created in the data directory => HTML and json file from csv

This code is not perfect but it has some good points:

- Well organized and easy to understand.
- Usability and extensibility.
- Clean code and commented as possible.
- Dockerized.

Bad points:

- Not well tested.
- Errors not handled well.



