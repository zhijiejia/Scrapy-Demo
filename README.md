# Scrapy-Demo

## 0. 安装
```python
pip install scrapy
```

## 1. 创建项目
```python
scrapy startproject projectName
```

### 2. 创建文件
```python
cd projectName
scrapy genspider bilibili bilibili.com        
# 在spiders文件夹下会创建一个 bilibili.py 的文件, 用于爬取bilibili的内容, 同时bilibili也会成为该爬虫的Name
```

### 3. 完善解析代码
```python
#在对应的Spider文件中, 需要完善parse函数, 其内部实现的是对指定url的具体解析

def parse(self, response):
    hrefs = response.xpath('//div[@class="bili-video-card__info--right"]/a/@href').extract()                                                    # 获取指定节点的属性内容 
    titles = response.xpath('//div[@class="bili-video-card__info--right"]//h3/@title').extract()                                                # 获取指定节点的属性内容
    texts = response.xpath('//div[@class="bili-video-card__info--right"]//a[@class="bili-video-card__info--owner"]/span/text()').extract()      # 获取指定节点的文本内容

#只用xpath路径搜索到的结果是selector对象, 其节点是selector的data属性, 而extract和extract_first就是抽取data属性, get()和extract_fitst()效果相同, getall()和extract()效果相同

getall() / extract(): 返回一个数组list, 里面包含了多个string, 如果只有一个string, 则返回['ABC']这样的形式   

get() / extract_first(): 返回一个string字符串, 是list数组里面的第一个字符串
```
