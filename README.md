<a href="https://github.com/lk-geimfari/rmanns/">
    <p align="center">
      <img src="https://raw.githubusercontent.com/lk-geimfari/rmanns/master/logo.png">
    </p>
</a>


**rmanns** (**r**e**m**ove **ann**otation**s**) - a small wrapper around `pdftk` for removing annotations from the pdf e-books downloaded from the popular web sites, such as [www.it-ebooks.info](www.it-ebooks.info) and [www.allitebooks.com](www.allitebooks.com).

Always before i buy books i download it from the internet and read the samples, for quality assessment. If I like the book - I buy it, if not, I do not buy it. Yeah, maybe it's not cool, but i don't want pay for bad books. The problems with books from the internets is annotations (red annotations is really irritable).

## How to use

As i say above, this script is just a wrapper around `pdftk` and it's mean that you should install `pdftk`:

```
➜ sudo apt update
➜ sudo apt install pdftk
```

Now you can use this script. You should move all your books with annotations to one folder and run script:
```
➜ python3 rmanns.py

Are you sure? [y/n]: y
Annotations removed from file: Learning_Python.pdf.
Annotations removed from file: Introducing_Data_Science.pdf.
```

Annotation will be deleted from all files that are in the current directory.


You can simply add alias for this script to your `~/.bashrc` or `~/.zshrc` file:

```bash
alias rmanns="python3 ~/.rmanns.py"
```

## License
MIT License
