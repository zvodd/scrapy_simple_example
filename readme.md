### install 

```bash
pip install scrapy scrapyd
```


### running

 simple run spider

```bash
scrapy crawl example -a target_url="https://doc.scrapy.org/en/latest/intro/tutorial.html"
```

with scrapyd

```bash
scrapyd
curl http://localhost:6800/schedule.json -d project=default -d spider=example -d target_url="https://doc.scrapy.org/en/latest/intro/tutorial.html"
```