#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import json
import datetime

reload(sys)
sys.setdefaultencoding('utf8') 

lib = os.path.abspath('.')
sys.path.append(lib)
import short
import content

class blog:
    def __init__(self, rootPath = '.'):
        self.__rootPath = rootPath
        self.__dirNames = ['db', 'css', 'js', 'img', 'template', 'attachment', 'articles']
        self.__defaultFileName = 'README.md'
        self.__defaultAppendix = '.html'

        self.__tagDBFileName = '/db/tag'
        self.__categotyDBFileName = '/db/category'
        self.__archiveDBFileName = '/db/archive'
        self.__articleDBFileName = '/db/article'

        self.__articleTpl = '/template/article.html.tpl'
        self.__indexTpl = '/template/index.html.tpl'
        
        self.__init();
    
    def __initDB(self, target):
        targetFilePath = self.__rootPath + target
        existtarget = '{}'
        
        if os.path.isfile(targetFilePath):
            targetFile = open(targetFilePath, 'r')
            existtarget = "".join(targetFile.readlines())
            if existtarget.strip() == "":
                existtarget = '{}'
            targetFile.close()
        
        return json.loads(existtarget)

    def __updateDB(self, target, content):
        targetFilePath = self.__rootPath + target
        existtargetDic = self.__initDB(target)
        targetList = content.decode('utf-8').split(',')
        itemval = self.__yearStr + '/' + self.__monthStr + '/' + self.__id

        for targetItem in targetList:
            targetItem = targetItem.strip()
            if targetItem == '':
                continue

            if targetItem in existtargetDic:
                if itemval not in existtargetDic[targetItem]:
                    existtargetDic[targetItem].append(itemval)
            else:
                existtargetDic[targetItem] = [self.__yearStr + '/' + self.__monthStr + '/' + self.__id]

        existtarget = json.dumps(existtargetDic, encoding='utf-8')
        targetFile = open(targetFilePath, 'w')
        targetFile.write(existtarget)
        targetFile.close()
    
    def __updateTagDB(self, tag):
        self.__updateDB(self.__tagDBFileName, tag)
        self.__tagStr = tag.replace('\n','')

    def __updateCategoryDB(self, category):
        self.__updateDB(self.__categotyDBFileName, category)
        self.__categoryStr = category.replace('\n','')

    def __updateArchiveDB(self):
        archiveFilePath = self.__rootPath + '/' + self.__archiveDBFileName
        existArchiveDic = self.__initDB(self.__archiveDBFileName)
        archiveKey = self.__yearStr + '/' + self.__monthStr
        if archiveKey in existArchiveDic:
            if self.__id not in existArchiveDic[archiveKey]:
                existArchiveDic[archiveKey].append(self.__id)
        else:
            existArchiveDic[archiveKey] = [self.__id]

        existArchive = json.dumps(existArchiveDic, encoding='utf-8')
        archiveFile = open(archiveFilePath, 'w')
        archiveFile.write(existArchive)
        archiveFile.close()
    
    def __updateArticleDB(self):
        articleFilePath = self.__rootPath + self.__articleDBFileName
        existArticleDic = self.__initDB(self.__articleDBFileName)
        articleObj = {}
        articleObj['tag'] = self.__tagStr
        articleObj['category'] = self.__categoryStr
        articleObj['title'] = self.__articleTitle
        articleObj['post'] = self.__postTimeStr
        articleObj['id'] = self.__id

        existArticleDic[self.__id] = articleObj
        existArticleDic[self.__articleFileName] = articleObj
        
        existArticle = json.dumps(existArticleDic, encoding='utf-8')
        articleFile = open(articleFilePath, 'w')
        articleFile.write(existArticle)
        articleFile.close()

    def __updateIndexPage(self):
        pass

    def __fill(self, title, category, tag, text):
        self.__articleTitle   = title.replace('\n','')
        articleContent = "".join(text)
        
        # Parse the content to html using template engine
        articleHtml = content.parse(articleContent)
        
        data             = {}
        data['title']    = self.__articleTitle
        data['icon']     = ''
        data['content']  = articleHtml
        data['post']     = self.__postTimeStr
        data['tag']      = tag
        data['category'] = category

        data['tag_html'] = '' 
        tagList = tag.split(',')
        for t in tagList:
            if t.strip() != '': 
                data['tag_html'] += '<a href="">' + t + '</a>'
        
        data['category_html'] = '' 
        cateList = category.split(',')
        for t in cateList:
            if t.strip() != '': 
                data['category_html'] += '<a href="">' + t + '</a>'

        # Read the article template
        articleTplFile = open(self.__rootPath + self.__articleTpl, 'r')
        articleTpl = "".join(articleTplFile.readlines())

        htmlPage = content.fill(data, articleTpl)

        # Write html page to disk
        htmlPageFile = open(self.__rootPath + '/' + self.__yearStr + '/' + self.__monthStr + '/' + self.__id + self.__defaultAppendix, 'w')
        htmlPageFile.write(htmlPage)
        htmlPageFile.close()
   
    def __parseTimeStr(self, postTimeStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.__postTimeStr = postTimeStr
        firstSepPos = self.__postTimeStr.find('-')
        self.__yearStr = self.__postTimeStr[0:firstSepPos]
        self.__monthStr = self.__postTimeStr[firstSepPos + 1:self.__postTimeStr.find('-', firstSepPos + 1)]

    def __init(self):
        """
        Create all derectories for your static blog
        """
        for dirName in self.__dirNames:
            targetDir = self.__rootPath + '/' + dirName
            if not os.path.exists(targetDir):
                os.mkdir(targetDir)
                f = open(targetDir + '/' + self.__defaultFileName, 'w')
                f.write('403\n')
                f.close()

        # Get current date time and create archive dir
        self.__parseTimeStr()
        if not os.path.exists(self.__rootPath + '/' + self.__yearStr):
            os.mkdir(self.__rootPath + '/' + self.__yearStr)
            if not os.path.exists(self.__rootPath + '/' + self.__yearStr + '/' + self.__monthStr):
                os.mkdir(self.__rootPath + '/' + self.__yearStr + '/' + self.__monthStr)
    
    def __genID(self, key): 
        ids = short.mapping(key)
        #Check the id whether has existed
        keys = self.__initDB(self.__articleDBFileName).keys()
        while True:
            for canId in ids:
                if canId not in keys:
                    return canId

    def create(self, articleFileName):
        """
        Create a article with using textile markup language.
        Here is the template description:
            LINE 1: article title
            LINE 2: category list, seperated with comma or space
            LINE 3: tag list, seperated with comma or space
            ...Begin here you can use textile markup language to write your blog
            ...Also ala supports github style:
                ```java
                YOUR CORE IS HERE
                ```
            ....Something else...
        """
        self.__articleFileName = articleFileName
	
        articleIDs = self.__initDB(self.__articleDBFileName).keys()
        if self.__articleFileName in articleIDs:
            print 'Please use [update] to replace [create].'
            return 0
        self.__id = self.__genID(self.__articleFileName)        
        aricleFile = open(self.__rootPath + '/articles/' + self.__articleFileName)
        articleContent = aricleFile.readlines()
        self.__updateTagDB(articleContent[2])
        self.__updateCategoryDB(articleContent[1])
        self.__updateArchiveDB()
        self.__fill(articleContent[0], articleContent[1], articleContent[2], articleContent[3:])
        self.__updateArticleDB()

    def remove(self, articleFileName):
        """
        Remove the article with this name
        """
        pass
    def __remove(self, articleFileName):
        # DB:
        #  remove tag
        #  remove category
        #  remove archive
        #  remove article
        # Remove the html
        pass

    def update(self, articleFileName):
        """
        Update the article with this name
        """
        self.__articleFileName = articleFileName
        articleDic = self.__initDB(self.__articleDBFileName)
        self.__id = articleDic[self.__articleFileName]['id']
        self.__parseTimeStr(articleDic[self.__articleFileName]['post'])
        
        aricleFile = open(self.__rootPath + '/articles/' + self.__articleFileName)
        articleContent = aricleFile.readlines()

        self.__updateTagDB(articleContent[2])
        self.__updateCategoryDB(articleContent[1])
        self.__updateArchiveDB()
        self.__fill(articleContent[0], articleContent[1], articleContent[2], articleContent[3:])
        self.__updateArticleDB()

if __name__ == '__main__':
    if sys.argv.__len__() > 2:
        b = blog()
        if sys.argv[1] == 'create':
            b.create(sys.argv[2])
        elif sys.argv[1] == 'update':
            b.update(sys.argv[2])
        else:
            b.remove(sys.argv[2])
    else:
        print 'blog.py [create|update|remove] textile_file'
