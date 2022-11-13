#  Earth Science people hanging out on Mastodon

This repository is a fork is of a [fork](https://github.com/oliviodare/mastodon-hps) of a [fork](https://jwyg.github.io/mastodon-sts/) of this [list of sociologists](https://www.perspektivbrocken.org/en/2022/10/28/sociologists-on-mastodon-a-list/). Any weirdness is due to my inept tweaking. 

The resulting [website](https://all-geo.org/mastodon-earthsci/) allows you to create a csv-file that can be uploaded in your mastodon settings, in order to follow every account on the list, or a selected subset.

Feel free to fork further though you might benefit from forking closer to the source (where they also publish to a Github page). There are two files that you will need to change. The Text in index.html and the accounts that are stored in resources/earthodons.csv (you can change the filename in assets/js/createcsv.js, too).

## Documentation

### csv file

the csv file is stored in /resources/.
Any file with the columns: `account`,`name`,`url` will do.

## License

The repository can be used under GNU General Public License v3, except the /resources/hpsers.csv file, which can only be used with explicit permission by the authors.
