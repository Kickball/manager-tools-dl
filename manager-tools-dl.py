#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, re, os, urllib2, argparse

parser = argparse.ArgumentParser(description='Scraper script for Managers Tools. (https://www.manager-tools.com/)')
group = parser.add_mutually_exclusive_group()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
    action="store_true")
group.add_argument("-r", "--resume", help="resume past download",
    action="store_true")
group.add_argument("-nd", "--no-download", help="don\'t download podcasts",
                    action="store_true")
parser.add_argument("-t", "--type", help="type of podcasts to download",
                    type=str, choices=['manager', 'career', 'all'])
parser.add_argument("-o", "--output-directory", help="podcast download directory",
                    type=str)

args = parser.parse_args()

no_download = args.no_download
verbose = args.verbose
resume = args.resume
output_directory = args.output_directory
type = args.type

def retrive_page_urls(content_url):
    if verbose:
        print "Attempting to open \'" + url_file + "\' -",
    file = open(url_file,'w')
    if verbose:
        print "done."

    if verbose:
        print "Attempting to fetch url (" + content_url + ") -",
    r = requests.get(content_url)
    if verbose:
        print "done."
    content = r.text
    page_urls = re.findall(general_url_regex, content)

    if verbose:
        print "Found " + str(len(page_urls)) +" page urls."

    if verbose:
        print "Writing urls to file \'" + url_file + "\' -",
    for page_url in page_urls:
        file.write('https://www.manager-tools.com' + page_url + '\n')
    file.close()
    if verbose:
        print "done.\n"

def generate_content_url(type):
    try:
        return {
            'manager': 'https://www.manager-tools.com/all-podcasts?field_content_domain_tid=4',
            'career': 'https://www.manager-tools.com/all-podcasts?field_content_domain_tid=5',
            'all': 'https://www.manager-tools.com/all-podcasts?field_content_domain_tid=All'
        }[type]
    except KeyError:
        if (verbose):
            try:
                print 'Invalid arguement of \'' + type + '\', defaulting podcast download type to all.'
            except:
                print 'No type arguement detected, defaulting podcast download type to all.'
        else:
            print 'Invalid arguement detected, defaulting type to all.'
        return 'https://www.manager-tools.com/all-podcasts?field_content_domain_tid=All'

def read_podcast_urls(file):
    if verbose:
        print "Reading urls from file \'" + file + "\' -",
    urls = open(file).readlines()
    if verbose:
        print "done.\n"

    return urls

def download_podcasts(urls):
    count = 1

    for url in urls:
        url = url[:-1] #Remove Line Break
        if verbose:
            print "Downloading " + url
        r2 = requests.get(url)
        podcast_page_content = r2.text
        if verbose:
            print "Checking " + url
        title = re.findall(title_regex, podcast_page_content)
        title = title[0].split('>')[1].split('<')[0]
        podcast_url = re.findall(podcast_url_regex, podcast_page_content)
        if (len(podcast_url) > 0):
            if verbose:
                print "Podcast found (" + title + ")!"
            print 'Downloading ' + title + ' -',
            podcast_url = podcast_url[0][:-2]
            podcast_file = urllib2.urlopen(podcast_url)
            output = open(os.path.join(output_directory, title + '.mp3'),'wb')
            output.write(podcast_file.read())
            output.close()
            print 'done.\n'
        with open(url_file, 'w') as f2:
            f2.writelines(urls[count:])
        count = count + 1

url_file = 'url_list.txt'

general_url_regex = re.compile('(\/20[\w\/-]*)')
title_regex = re.compile('<h1 class=\"title\" id=\"page-title\">.+</h1>')
podcast_url_regex = re.compile('https://www.manager-tools.com/system/files/podcast/mp3\/.*.mp3" ')

if (resume == False):
    content_url = generate_content_url(type)
    if verbose:
        print "Content url set to: " + content_url + "\n"

    retrive_page_urls(content_url)

if (no_download == False):
    urls = read_podcast_urls(url_file)

    download_podcasts(urls)
