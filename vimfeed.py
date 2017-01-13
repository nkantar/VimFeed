from operator import itemgetter

from dateutil.parser import parse
import feedparser
from jinja2 import Environment, PackageLoader
import yaml

def timestamp(value, format='%Y-%m-%d %A'):
    return parse(value).strftime(format)

def extract_entries(feed):
    return [{'feed_title': feed['channel']['title'],
             'feed_link': feed['channel']['link'],
             'entry_title': entry['title'],
             'entry_link': entry['link'],
             'entry_timestamp': parse(entry['updated']).isoformat()}
            for entry
            in feed['items']]

def parse_feeds():
    environment = Environment(loader=PackageLoader('vimfeed', 'templates'))
    environment.filters['timestamp'] = timestamp
    feeds = []
    entries = []
    with open('feeds.yaml') as f:
        urls = yaml.load(f)
        for url in urls:
            try:
                feed = feedparser.parse(url['feed_url'])
                feeds.append({'title': url['site_name'], 'url': url['site_url']})
                if len(feed['feed']) > 0:
                    entries.extend(extract_entries(feed))
            except Exception as e:
                print('Feed parsing failed!')
                print(e)
                print('URL: %s' % url)
    sorted_entries = sorted(entries, key=itemgetter('entry_timestamp'), reverse=True)
    sorted_feeds = sorted(feeds, key=itemgetter('title'))
    templates = ['feed.atom', 'index.html', 'about/index.html', 'list/index.html']
    for template_filename in templates:
        template = environment.get_template(template_filename)
        result = template.render(feeds=sorted_feeds, entries=sorted_entries).encode('ascii', 'ignore')
        with open('build/%s' % template_filename, 'w') as ff:
            ff.write(result.decode('utf-8').replace('\\n', ''))

if __name__ == '__main__':
    parse_feeds()

