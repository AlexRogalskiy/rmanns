<a href="https://github.com/lk-geimfari/rmanns/">
    <p align="center">
      <img src="https://raw.githubusercontent.com/lk-geimfari/rmanns/master/logo.png">
    </p>
</a>


Always before i buy books i have downloaded it from the internet and read the samples, for quality assessment. If I like the book - I buy it, if not, I do not buy it. Yeah, maybe it's not cool, but i don't want pay for bad books. 
The problems with books from the internets is annotations. Maybe they irritate only me. 
Anyway, i have written this simple wrapper around pdftk for removing annotations from the books from 
the popular pirate web sites, such as [www.it-ebooks.info ](http://www.it-ebooks.info ) and [www.allitebooks.com](http://www.allitebooks.com).


## How to use

As i say, this script is just a wrapper around `pdftk` and it's mean that you should install `pdftk`:

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
