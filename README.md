# VimFeed

Vim news from 'round the world.

## Wat

![VimFeed logo](https://vimfeed.github.io/assets/images/vimfeed152.png)


[**VimFeed**](https://vimfeed.github.io) is an aggregated feed populated with Vim content from a variety of sources.

It is very much a contributions-welcome project, so if you have any great resources (be they your own or not), please submit them via issues or pull requests.

## How does it work?

The main script (`vimfeed.py`) reads URLs from `feeds.yaml` one by one, and for each collects the published posts. All the posts are combined into one giant list and sorted by date (newest first). Once all this data is ready to go, templates inside `templates/` are used to generate `index.html`, `about/index.html`, `list/index.html`, and `feed.atom` inside `build/`, and those files are then pushed to the `gh-pages` branch, which causes [GitHub Pages](https://pages.github.com) to generate the published site.

## I've got a cool Vim blog and want to add it to VimFeed.

Excellent&mdash;submit a pull request with it being added to `feeds.yaml`. Please do try to submit only Vim content, so if you write about tons of other stuff as well, it may be better to submit a tag/category-specific feed.

Please also do test your feed if at all possible, and make sure it's all parsed fine and everything looks copacetic.

Bonus points for getting the author's permission, too!

## I've got a feature request and/or bug report.

Please [submit an issue](https://github.com/VimFeed/VimFeed/issues/new).

## How can I help?

Suggestions for feeds to include would be great. It may sound silly, but this whole thing is useless without a decent amount of content.

Also welcome are code contributions, documentation updates, and even code reviews.

A good place for any of the above would probably be a [new issue](https://github.com/VimFeed/VimFeed/issues/new).

## Why do you like Vim so much?

Because it's awesome.

## This whole thing sucks.

Care to [elaborate](https://github.com/VimFeed/VimFeed/issues/new)?

