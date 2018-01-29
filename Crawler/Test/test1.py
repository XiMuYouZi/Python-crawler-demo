from  pyquery import PyQuery as pq

html = """



<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="ua-mac ua-webkit book-new-nav">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>
  豆瓣图书标签: 小说
</title>
  
<script>!function(e){var o=function(o,n,t){var c,i,r=new Date;n=n||30,t=t||"/",r.setTime(r.getTime()+24*n*60*60*1e3),c="; expires="+r.toGMTString();for(i in o)e.cookie=i+"="+o[i]+c+"; path="+t},n=function(o){var n,t,c,i=o+"=",r=e.cookie.split(";");for(t=0,c=r.length;t<c;t++)if(n=r[t].replace(/^\s+|\s+$/g,""),0==n.indexOf(i))return n.substring(i.length,n.length).replace(/\"/g,"");return null},t=e.write,c={"douban.com":1,"douban.fm":1,"google.com":1,"google.cn":1,"googleapis.com":1,"gmaptiles.co.kr":1,"gstatic.com":1,"gstatic.cn":1,"google-analytics.com":1,"googleadservices.com":1},i=function(e,o){var n=new Image;n.onload=function(){},n.src="https://www.douban.com/j/except_report?kind=ra022&reason="+encodeURIComponent(e)+"&environment="+encodeURIComponent(o)},r=function(o){try{t.call(e,o)}catch(e){t(o)}},a=/<script.*?src\=["']?([^"'\s>]+)/gi,g=/http:\/\/(.+?)\.([^\/]+).+/i;e.writeln=e.write=function(e){var t,l=a.exec(e);return l&&(t=g.exec(l[1]))?c[t[2]]?void r(e):void("tqs"!==n("hj")&&(i(l[1],location.href),o({hj:"tqs"},1),setTimeout(function(){location.replace(location.href)},50))):void r(e)}}(document);
</script>

  
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
  
  <script>var _head_start = new Date();</script>
  
  <link href="https://img3.doubanio.com/f/book/c562010083631a8b5625ac07bc2a6e7e4466b6f6/css/book/master.css" rel="stylesheet" type="text/css">

  <link href="https://img3.doubanio.com/f/book/8a9d097c416aabac4f7e45f5d2ce9c6834b3fc7a/css/book/base/init.css" rel="stylesheet">
  <style type="text/css"></style>
  <script src="https://img3.doubanio.com/f/book/0495cb173e298c28593766009c7b0a953246c5b5/js/book/lib/jquery/jquery.js"></script>
  <script src="https://img3.doubanio.com/f/book/0f1957d4c436280f238b0295e4d0ba6855510555/js/book/master.js"></script>
  

  
  <script>  </script>
  <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/28fc3e84f96f7794.css">

  <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>
<body>
  
    <script>var _body_start = new Date();</script>
    
  



    <link href="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <ul>
    <li>
    <a id="top-nav-doumail-link" href="https://www.douban.com/doumail/">豆邮</a>
    </li>
    <li class="nav-user-account">
      <a target="_blank" href="https://www.douban.com/accounts/" class="bn-more">
        <span>西木柚子的帐号</span><span class="arrow"></span>
      </a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://www.douban.com/mine/">个人主页</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/orders/">我的订单</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/wallet/">我的钱包</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/accounts/">帐号管理</a>
              </td>
            </tr>
            <tr>
              <td>
                <a href="https://www.douban.com/accounts/logout?source=book&ck=_msq">退出</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  <div class="top-nav-reminder">
    <a href="https://www.douban.com/notification/" class="lnk-remind">提醒</a>
    <div id="top-nav-notimenu" class="more-items">
      <div class="bd">
        <p>加载中...</p>
      </div>
    </div>
  </div>

    
<div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="slogan">我们的精神角落</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
    <div id="doubanapp-tip">
      <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 5.0 全新发布</a>
      <a href="javascript: void 0;" class="tip-close">×</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;42279477&quot;}">豆瓣</a>
    </li>
    <li class="on">
      <a href="https://book.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;42279477&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;42279477&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;42279477&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;42279477&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;42279477&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;42279477&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;42279477&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;42279477&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;42279477&quot;}">市集</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;42279477&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    USER_ID: "42279477",
    UPLOAD_AUTH_TOKEN: "42279477:8b22dec856b4355d11d2f08ec54d821c29b92a7e",
    SSE_TOKEN: "ab8a67e7429303effe306609fb05405c28cbbaf1",
    SSE_TIMESTAMP: "1517200161",
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.js" defer="defer"></script>




  



    <link href="//img3.doubanio.com/dae/accounts/resources/094108a/book/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-book" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;book.douban.com">豆瓣读书</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;book.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="书名、作者、ISBN" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1001" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://book.douban.com/mine"
     >我读</a>
    </li>
    <li    ><a href="https://book.douban.com/updates"
     >动态</a>
    </li>
    <li    ><a href="https://book.douban.com/recommended"
     >豆瓣猜</a>
    </li>
    <li    ><a href="https://book.douban.com/tag/"
     >分类浏览</a>
    </li>
    <li    ><a href="https://book.douban.com/cart/"
     >购书单</a>
    </li>
    <li    ><a href="https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban"
            target="_blank"
     >电子图书</a>
    </li>
    <li    ><a href="https://market.douban.com/book?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web"
     >豆瓣书店</a>
    </li>
    <li    ><a href="https://book.douban.com/annual/2017?source=navigation"
            target="_blank"
     >2017年度榜单</a>
    </li>
    <li    ><a href="https://book.douban.com/standbyme/2017?source=navigation"
            target="_blank"
     >2017读书报告</a>
    </li>
    <li          class=" book-cart"
    ><a href="https://market.douban.com/cart/?utm_campaign=book_nav_cart&utm_source=douban&utm_medium=pc_web"
            target="_blank"
     >购物车</a>
    </li>
  </ul>
</div>

  </div>
    <a href="https://book.douban.com/annual/2017?source=patch" class="bookannual2017"></a>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'book_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= pic}}" width="40" />
            <div>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                <p>
                {{if type == "b"}}
                    {{= author_name}}
                {{else type == "a" }}
                    {{if en_name}}
                        {{= en_name}}
                    {{/if}}
                {{/if}}
                 </p>
            </div>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/094108a/book/bundle.js" defer="defer"></script>





    <div id="wrapper">
        
        
  <div id="content">
    
    <h1>豆瓣图书标签: 小说</h1>

    <div class="grid-16-8 clearfix">
      
      <div class="article">
  <div id="subject_list">

      
  
  
  <div class="clearfix">
    <span class="rr greyinput">

          综合排序
          &nbsp;/&nbsp;

          <a href="/tag/%E5%B0%8F%E8%AF%B4?type=R">按出版日期排序</a>
          &nbsp;/&nbsp;

          <a href="/tag/%E5%B0%8F%E8%AF%B4?type=S">按评价排序</a>
    </span>
  </div>



    
  
  <ul class="subject-list">
      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/2230208/" 
  onclick="moreurl(this,{i:'0',query:'',subject_id:'2230208',from:'book_subject_search'})">
        <img class="" src="https://img1.doubanio.com/mpic/s2720819.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/2230208/" title="我的前半生" 
  onclick="moreurl(this,{i:'0',query:'',subject_id:'2230208',from:'book_subject_search'})">

    我的前半生


    

  </a>

      </h2>
      <div class="pub">
        
  
  亦舒 / 新世界出版社 / 2007-8 / 22.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar40"></span>
        <span class="rating_nums">7.9</span>

    <span class="pl">
        (21897人评价)
    </span>
  </div>



        
  
  
  
    <p>一个三十几岁的美丽女人子君，在家做全职家庭主妇。却被一个平凡女人夺走丈夫，一段婚姻的失败，让女主角不得不坚强，变得更美丽，有了事业，最终遇见一个更值得爱的男... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=2230208" name="sbtn-2230208-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=2230208" name="sbtn-2230208-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=2230208" name="sbtn-2230208-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="2230208">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="2230208" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/6082808/" 
  onclick="moreurl(this,{i:'1',query:'',subject_id:'6082808',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s6384944.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/6082808/" title="百年孤独" 
  onclick="moreurl(this,{i:'1',query:'',subject_id:'6082808',from:'book_subject_search'})">

    百年孤独


    

  </a>

      </h2>
      <div class="pub">
        
  
  [哥伦比亚] 加西亚·马尔克斯 / 范晔 / 南海出版公司 / 2011-6 / 39.50元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.2</span>

    <span class="pl">
        (124018人评价)
    </span>
  </div>



        
  
  
  
    <p>《百年孤独》是魔幻现实主义文学的代表作，描写了布恩迪亚家族七代人的传奇故事，以及加勒比海沿岸小镇马孔多的百年兴衰，反映了拉丁美洲一个世纪以来风云变幻的历史。... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=6082808" name="sbtn-6082808-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=6082808" name="sbtn-6082808-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=6082808" name="sbtn-6082808-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
              <span class="market-info">
                <a href="https://book.douban.com/subject/6082808/?channel=subject_list&amp;platform=web" target="_blank">在豆瓣购买</a>
              </span>
              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="6082808">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="6082808" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1770782/" 
  onclick="moreurl(this,{i:'2',query:'',subject_id:'1770782',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s1727290.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1770782/" title="追风筝的人" 
  onclick="moreurl(this,{i:'2',query:'',subject_id:'1770782',from:'book_subject_search'})">

    追风筝的人


    

  </a>

      </h2>
      <div class="pub">
        
  
  [美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">8.9</span>

    <span class="pl">
        (300438人评价)
    </span>
  </div>



        
  
  
  
    <p>12岁的阿富汗富家少爷阿米尔与仆人哈桑情同手足。然而，在一场风筝比赛后，发生了一件悲惨不堪的事，阿米尔为自己的懦弱感到自责和痛苦，逼走了哈桑，不久，自己也跟... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=1770782" name="sbtn-1770782-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=1770782" name="sbtn-1770782-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=1770782" name="sbtn-1770782-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
              <span class="market-info">
                <a href="https://book.douban.com/subject/1770782/?channel=subject_list&amp;platform=web" target="_blank">在豆瓣购买</a>
              </span>
              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1770782">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1770782" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  
    
    
  <div class="ebook-link">
    <a target="_blank" href="https://read.douban.com/ebook/1162265/?dcs=tag-buylink&amp;dcm=douban&amp;dct=1770782">去看电子版</a>
  </div>
  


      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/4820710/" 
  onclick="moreurl(this,{i:'3',query:'',subject_id:'4820710',from:'book_subject_search'})">
        <img class="" src="https://img1.doubanio.com/mpic/s4371408.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/4820710/" title="1984" 
  onclick="moreurl(this,{i:'3',query:'',subject_id:'4820710',from:'book_subject_search'})">

    1984


    

  </a>

      </h2>
      <div class="pub">
        
  
  [英] 乔治·奥威尔 / 刘绍铭 / 北京十月文艺出版社 / 2010-4-1 / 28.00

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.3</span>

    <span class="pl">
        (42425人评价)
    </span>
  </div>



        
  
  
  
    <p>★村上春树以《1Q84》向本书致敬
★著名学者刘绍铭经典译本内地首次出版
★62种文字风靡110个国家，全球销量超过5000万册
★《时代周刊》“最好的10... </p>






      <div class="ft">
          
  <div class="collect-info">
      
        <span>我想读这本书</span>

        
        
        <span>
          <a href="do/42279477/update?add=4820710" name="sbtn-4820710-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=4820710" name="sbtn-4820710-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
              <span class="market-info">
                <a href="https://book.douban.com/subject/25708359/?channel=subject_list&amp;platform=web" target="_blank">在豆瓣购买</a>
              </span>
              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="4820710">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="4820710" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1858513/" 
  onclick="moreurl(this,{i:'4',query:'',subject_id:'1858513',from:'book_subject_search'})">
        <img class="" src="https://img1.doubanio.com/mpic/s2659208.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1858513/" title="月亮和六便士" 
  onclick="moreurl(this,{i:'4',query:'',subject_id:'1858513',from:'book_subject_search'})">

    月亮和六便士


    

  </a>

      </h2>
      <div class="pub">
        
  
  [英] 毛姆 / 傅惟慈 / 上海译文出版社 / 2006-8 / 15.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.0</span>

    <span class="pl">
        (74873人评价)
    </span>
  </div>



        
  
  
  
    <p>一个英国证券交易所的经纪人，本已有牢靠的职业和地位、美满的家庭，但却迷恋上绘画，像“被魔鬼附了体”，突然弃家出走，到巴黎去追求绘画的理想。他的行径没有人能够... </p>






      <div class="ft">
          
  <div class="collect-info">
      
        <span>我想读这本书</span>

        
        
        <span>
          <a href="do/42279477/update?add=1858513" name="sbtn-1858513-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=1858513" name="sbtn-1858513-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1858513">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1858513" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1082154/" 
  onclick="moreurl(this,{i:'5',query:'',subject_id:'1082154',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s23836852.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1082154/" title="活着" 
  onclick="moreurl(this,{i:'5',query:'',subject_id:'1082154',from:'book_subject_search'})">

    活着


    

  </a>

      </h2>
      <div class="pub">
        
  
  余华 / 南海出版公司 / 1998-5 / 12.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.1</span>

    <span class="pl">
        (140112人评价)
    </span>
  </div>



        
  
  
  
    <p>地主少爷福贵嗜赌成性，终于赌光了家业一贫如洗，穷困之中的福贵因为母亲生病前去求医，没想到半路上被国民党部队抓了壮丁，后被解放军所俘虏，回到家乡他才知道母亲已... </p>






      <div class="ft">
          
  <div class="collect-info">
      
        <span>我读过这本书</span>

  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1082154">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1082154" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1008145/" 
  onclick="moreurl(this,{i:'6',query:'',subject_id:'1008145',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s1070222.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1008145/" title="围城" 
  onclick="moreurl(this,{i:'6',query:'',subject_id:'1008145',from:'book_subject_search'})">

    围城


    

  </a>

      </h2>
      <div class="pub">
        
  
  钱锺书 / 人民文学出版社 / 1991-2 / 19.00

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">8.9</span>

    <span class="pl">
        (194700人评价)
    </span>
  </div>



        
  
  
  
    <p>《围城》是钱钟书所著的长篇小说。第一版于1947年由上海晨光出版公司出版。1949年之后，由于政治等方面的原因，本书长期无法在中国大陆和台湾重印，仅在香港出... </p>






      <div class="ft">
          
  <div class="collect-info">
      
        <span>我读过这本书</span>

  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1008145">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1008145" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1200840/" 
  onclick="moreurl(this,{i:'7',query:'',subject_id:'1200840',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s2335693.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1200840/" title="平凡的世界（全三部）" 
  onclick="moreurl(this,{i:'7',query:'',subject_id:'1200840',from:'book_subject_search'})">

    平凡的世界（全三部）


    

  </a>

      </h2>
      <div class="pub">
        
  
  路遥 / 人民文学出版社 / 2005-1 / 64.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.0</span>

    <span class="pl">
        (104426人评价)
    </span>
  </div>



        
  
  
  
    <p>《平凡的世界》是一部现实主义小说，也是一部小说形式的家族史。作者浓缩了中国西北农村的历史变迁过程，在小说中全景式地表现了中国当代城乡的社会生活。在近十年的广... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=1200840" name="sbtn-1200840-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=1200840" name="sbtn-1200840-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=1200840" name="sbtn-1200840-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1200840">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1200840" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/4908885/" 
  onclick="moreurl(this,{i:'8',query:'',subject_id:'4908885',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s4468484.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/4908885/" title="局外人" 
  onclick="moreurl(this,{i:'8',query:'',subject_id:'4908885',from:'book_subject_search'})">

    局外人


    

  </a>

      </h2>
      <div class="pub">
        
  
  [法] 阿尔贝·加缪 / 柳鸣九 / 上海译文出版社 / 2010-9 / 22.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.0</span>

    <span class="pl">
        (33152人评价)
    </span>
  </div>



        
  
  
  
    <p>《局外人》是加缪小说的成名作和代表作之一，堪称20世纪整个西方文坛最具有划时代意义最著名小说之一，“局外人”也由此成为整个西方文学-哲学中最经典的人物形象和... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=4908885" name="sbtn-4908885-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=4908885" name="sbtn-4908885-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=4908885" name="sbtn-4908885-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
              <span class="market-info">
                <a href="https://book.douban.com/subject/4908885/?channel=subject_list&amp;platform=web" target="_blank">在豆瓣购买</a>
              </span>
              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="4908885">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="4908885" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1856494/" 
  onclick="moreurl(this,{i:'9',query:'',subject_id:'1856494',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s2059791.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1856494/" title="卡拉马佐夫兄弟" 
  onclick="moreurl(this,{i:'9',query:'',subject_id:'1856494',from:'book_subject_search'})">

    卡拉马佐夫兄弟


    

  </a>

      </h2>
      <div class="pub">
        
  
  [俄]陀思妥耶夫斯基 / 荣如德 / 上海译文出版社 / 2006-8 / 25.00

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.4</span>

    <span class="pl">
        (7627人评价)
    </span>
  </div>



        
  
  
  
    <p>老卡拉马佐夫贪婪好色，独占妻子留给儿子们的遗产，并与长子德米特里为一个风流女子争风吃醋。一天黑夜，德米特里疑心自己的情人去跟老头儿幽会，便闯入家园，一怒之下... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=1856494" name="sbtn-1856494-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=1856494" name="sbtn-1856494-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=1856494" name="sbtn-1856494-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1856494">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1856494" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  
    
    
  <div class="ebook-link">
    <a target="_blank" href="https://read.douban.com/ebook/26004399/?dcs=tag-buylink&amp;dcm=douban&amp;dct=1856494">去看电子版</a>
  </div>
  


      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/2035162/" 
  onclick="moreurl(this,{i:'10',query:'',subject_id:'2035162',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s2347562.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/2035162/" title="刀锋" 
  onclick="moreurl(this,{i:'10',query:'',subject_id:'2035162',from:'book_subject_search'})">

    刀锋


    

  </a>

      </h2>
      <div class="pub">
        
  
  [英]毛姆 / 周煦良 / 上海译文出版社 / 2007-3 / 18.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.0</span>

    <span class="pl">
        (27870人评价)
    </span>
  </div>



        
  
  
  
    <p>威廉·萨默塞特·毛姆（1874-1965），英国著名小说家、戏剧家。《刀锋》是他的主要作品之一。
小说写一个参加第一次世界大战的美国青年飞行员拉里·达雷尔。... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=2035162" name="sbtn-2035162-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=2035162" name="sbtn-2035162-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=2035162" name="sbtn-2035162-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="2035162">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="2035162" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/2035171/" 
  onclick="moreurl(this,{i:'11',query:'',subject_id:'2035171',from:'book_subject_search'})">
        <img class="" src="https://img1.doubanio.com/mpic/s3983958.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/2035171/" title="人生的枷锁" 
  onclick="moreurl(this,{i:'11',query:'',subject_id:'2035171',from:'book_subject_search'})">

    人生的枷锁


    

  </a>

      </h2>
      <div class="pub">
        
  
  [英] 毛姆 / 张柏然、张增健、倪俊 / 上海译文出版社 / 2007-3 / 32.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.0</span>

    <span class="pl">
        (12439人评价)
    </span>
  </div>



        
  
  
  
    <p>《人生的枷锁》是毛姆的代表作，具有明显的自传色彩。
小说主人公菲利普·凯里自幼父母双亡，不幸又先天残疾，在冷漠而陌生的环境中度过了童年，性格因此孤僻而敏感。... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=2035171" name="sbtn-2035171-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=2035171" name="sbtn-2035171-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=2035171" name="sbtn-2035171-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="2035171">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="2035171" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1017143/" 
  onclick="moreurl(this,{i:'12',query:'',subject_id:'1017143',from:'book_subject_search'})">
        <img class="" src="https://img1.doubanio.com/mpic/s1091698.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1017143/" title="不能承受的生命之轻" 
  onclick="moreurl(this,{i:'12',query:'',subject_id:'1017143',from:'book_subject_search'})">

    不能承受的生命之轻


    

  </a>

      </h2>
      <div class="pub">
        
  
  [捷克] 米兰·昆德拉 / 许钧 / 上海译文出版社 / 2003-7 / 23.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">8.5</span>

    <span class="pl">
        (137821人评价)
    </span>
  </div>



        
  
  
  
    <p>《不能承受的生命之轻》是米兰·昆德拉最负盛名的作品。小说描写了托马斯与特丽莎、萨丽娜之间的感情生活。但它不是一个男人和两个女人的三角性爱故事，它是一部哲理小... </p>






      <div class="ft">
          
  <div class="collect-info">
      
        <span>我想读这本书</span>

        
        
        <span>
          <a href="do/42279477/update?add=1017143" name="sbtn-1017143-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=1017143" name="sbtn-1017143-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1017143">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1017143" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1085799/" 
  onclick="moreurl(this,{i:'13',query:'',subject_id:'1085799',from:'book_subject_search'})">
        <img class="" src="https://img1.doubanio.com/mpic/s9137567.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1085799/" title="白鹿原" 
  onclick="moreurl(this,{i:'13',query:'',subject_id:'1085799',from:'book_subject_search'})">

    白鹿原


    

  </a>

      </h2>
      <div class="pub">
        
  
  陈忠实 / 人民文学出版社 / 1997-12 / 28.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">8.6</span>

    <span class="pl">
        (44886人评价)
    </span>
  </div>



        
  
  
  
    <p>这是一部渭河平原五十年变迁的雄奇史诗，一轴中国农村班斓多彩、触目惊心的长幅画卷。主人公六娶六丧，神秘的序曲预示着不祥。一个家族两代子孙，为争夺白鹿原的统治代... </p>






      <div class="ft">
          
  <div class="collect-info">
      
        <span>我想读这本书</span>

        
        
        <span>
          <a href="do/42279477/update?add=1085799" name="sbtn-1085799-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=1085799" name="sbtn-1085799-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1085799">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1085799" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/2035179/" 
  onclick="moreurl(this,{i:'14',query:'',subject_id:'2035179',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s2347590.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/2035179/" title="动物农场" 
  onclick="moreurl(this,{i:'14',query:'',subject_id:'2035179',from:'book_subject_search'})">

    动物农场


    

  </a>

      </h2>
      <div class="pub">
        
  
  [英] 乔治·奥威尔 / 荣如德 / 上海译文出版社 / 2007-3 / 10.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.2</span>

    <span class="pl">
        (33565人评价)
    </span>
  </div>



        
  
  
  
    <p>《动物农场》是奥威尔最优秀的作品之一，是一则入木三分的反乌托的政治讽喻寓言。
农场的一群动物成功地进行了一场“革命”，将压榨他们的人类东家赶出农场，建立起一... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=2035179" name="sbtn-2035179-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=2035179" name="sbtn-2035179-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=2035179" name="sbtn-2035179-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="2035179">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="2035179" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/3406401/" 
  onclick="moreurl(this,{i:'15',query:'',subject_id:'3406401',from:'book_subject_search'})">
        <img class="" src="https://img1.doubanio.com/mpic/s6790238.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/3406401/" title="悉达多" 
  onclick="moreurl(this,{i:'15',query:'',subject_id:'3406401',from:'book_subject_search'})">

    悉达多


    

  </a>

      </h2>
      <div class="pub">
        
  
  [德] 赫尔曼·黑塞 / 杨玉功 译、丁君君 校 / 上海人民出版社 / 2009-3 / 20.00

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.0</span>

    <span class="pl">
        (13296人评价)
    </span>
  </div>



        
  
  
  
    <p>古印度贵族青年悉达多英俊聪慧，拥有人们羡慕的一切。为了追求心灵的安宁，他孤身一人展开了求道之旅。他在舍卫城聆听佛陀乔答摩宣讲教义，在繁华的大城中结识了名妓伽... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=3406401" name="sbtn-3406401-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=3406401" name="sbtn-3406401-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=3406401" name="sbtn-3406401-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="3406401">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="3406401" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1089243/" 
  onclick="moreurl(this,{i:'16',query:'',subject_id:'1089243',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s1076372.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1089243/" title="黄金时代" 
  onclick="moreurl(this,{i:'16',query:'',subject_id:'1089243',from:'book_subject_search'})">

    黄金时代


    
      <span style="font-size:12px;"> : 时代三部曲 </span>

  </a>

      </h2>
      <div class="pub">
        
  
  王小波 / 花城出版社 / 1999-3 / 19.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">8.8</span>

    <span class="pl">
        (59960人评价)
    </span>
  </div>



        
  
  
  
    <p>《黄金时代》是《时代三部曲》之一。  这是以文革时期为背景的系列作品构成的长篇。发生“文化大革命”的二十世纪六七十年代，正是我们国家和民族的灾难年代。那时，... </p>






      <div class="ft">
          
  <div class="collect-info">
      
        <span>我读过这本书</span>

  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1089243">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1089243" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1829226/" 
  onclick="moreurl(this,{i:'17',query:'',subject_id:'1829226',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s4007145.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1829226/" title="肖申克的救赎" 
  onclick="moreurl(this,{i:'17',query:'',subject_id:'1829226',from:'book_subject_search'})">

    肖申克的救赎


    

  </a>

      </h2>
      <div class="pub">
        
  
  [美] 斯蒂芬·金 / 施寄青、赵永芬、齐若兰 / 人民文学出版社 / 2006-7 / 29.90元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.1</span>

    <span class="pl">
        (39519人评价)
    </span>
  </div>



        
  
  
  
    <p>这本书收入斯蒂芬·金的四部中篇小说，是他作品中的杰出代表作。其英文版一经推出，即登上《纽约时报》畅销书排行榜的冠军之位，当年在美国狂销二十八万册。目前，这本... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=1829226" name="sbtn-1829226-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=1829226" name="sbtn-1829226-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=1829226" name="sbtn-1829226-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1829226">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1829226" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/5337248/" 
  onclick="moreurl(this,{i:'18',query:'',subject_id:'5337248',from:'book_subject_search'})">
        <img class="" src="https://img3.doubanio.com/mpic/s4526465.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/5337248/" title="台北人" 
  onclick="moreurl(this,{i:'18',query:'',subject_id:'5337248',from:'book_subject_search'})">

    台北人


    

  </a>

      </h2>
      <div class="pub">
        
  
  白先勇 / 广西师范大学出版社 / 2010-10 / 38.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">8.9</span>

    <span class="pl">
        (14052人评价)
    </span>
  </div>



        
  
  
  
    <p>作为20世纪中文小说100强的《台北人》，是一部深具复杂性的短篇小说集，由十四个一流的短篇小说构成，串联成一体，则效果遽然增加，不但小说之幅面变广，使我们看... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=5337248" name="sbtn-5337248-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=5337248" name="sbtn-5337248-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=5337248" name="sbtn-5337248-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  

    <span class="buy-info">
      <a href="https://book.douban.com/subject/5337248/buylinks">
        纸质版 156.00 元起
      </a>
    </span>

              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="5337248">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="5337248" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  
    
    
  <div class="ebook-link">
    <a target="_blank" href="https://read.douban.com/ebook/263569/?dcs=tag-buylink&amp;dcm=douban&amp;dct=5337248">去看电子版</a>
  </div>
  


      </div>

    </div>
  </li>
  

      
      
  
  <li class="subject-item">
    <div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1068920/" 
  onclick="moreurl(this,{i:'19',query:'',subject_id:'1068920',from:'book_subject_search'})">
        <img class="" src="https://img1.doubanio.com/mpic/s1078958.jpg"
          width="90">
      </a>
    </div>
    <div class="info">
      <h2 class="">
        
  
  <a href="https://book.douban.com/subject/1068920/" title="飘" 
  onclick="moreurl(this,{i:'19',query:'',subject_id:'1068920',from:'book_subject_search'})">

    飘


    

  </a>

      </h2>
      <div class="pub">
        
  
  [美国] 玛格丽特·米切尔 / 李美华 / 译林出版社 / 2000-9 / 40.00元

      </div>


        
  
  
  
  <div class="star clearfix">
        <span class="allstar45"></span>
        <span class="rating_nums">9.3</span>

    <span class="pl">
        (80512人评价)
    </span>
  </div>



        
  
  
  
    <p>小说中的故事发生在1861年美国南北战争前夕。生活在南方的少女郝思嘉从小深受南方文化传统的熏陶，可在她的血液里却流淌着野性的叛逆因素。随着战火的蔓廷和生活环... </p>






      <div class="ft">
          
  <div class="collect-info">
      

        
        
        <span>
          <a href="wish/42279477/update?add=1068920" name="sbtn-1068920-wish" class="j a_collect_btn" rel="nofollow">想读</a>
        </span>
        
        
        <span>
          <a href="do/42279477/update?add=1068920" name="sbtn-1068920-do" class="j a_collect_btn" rel="nofollow">在读</a>
        </span>
        
        
        <span>
          <a href="collection/42279477/update?add=1068920" name="sbtn-1068920-collect" class="j a_collect_btn" rel="nofollow">读过</a>
        </span>
  </div>


          <div class="cart-actions">
            
                
  


              
  <span class="cart-info">
    
  <span class="add2cartWidget ">
      
      <a href="javascript:;" class="j  a_add2cart add2cart"
        name="1068920">
        <span>加入购书单</span></a>
      <span class="color_gary book-in-cart hidden"
        >
          已在<a href="https://book.douban.com/cart">购书单</a>
        <a class="delete-cart-item" rel="1068920" href="https://book.douban.com/cart">删除</a>
      </span>
  </span>
  

  </span>

          </div>

            
            
  

      </div>

    </div>
  </li>
  

  </ul>


      
    
    
    
        <div class="paginator">
        <span class="prev">
            &lt;前页
        </span>
        
        

                <span class="thispage">1</span>
                
            <a href="/tag/小说?start=20&amp;type=T" >2</a>
        
                
            <a href="/tag/小说?start=40&amp;type=T" >3</a>
        
                
            <a href="/tag/小说?start=60&amp;type=T" >4</a>
        
                
            <a href="/tag/小说?start=80&amp;type=T" >5</a>
        
                
            <a href="/tag/小说?start=100&amp;type=T" >6</a>
        
                
            <a href="/tag/小说?start=120&amp;type=T" >7</a>
        
                
            <a href="/tag/小说?start=140&amp;type=T" >8</a>
        
                
            <a href="/tag/小说?start=160&amp;type=T" >9</a>
        
            <span class="break">...</span>
                
            <a href="/tag/小说?start=1960&amp;type=T" >99</a>
        
            <a href="/tag/小说?start=1980&amp;type=T" >100</a>
        
        <span class="next">
            <link rel="next" href="/tag/小说?start=20&amp;type=T"/>
            <a href="/tag/小说?start=20&amp;type=T" >后页&gt;</a>
        </span>

        </div>


  </div>
</div>
      <div class="aside">
        
  <br/>
  <div id="dale_book_tag_top_right"></div>

    
  

  <h2>
    <span class="">相关的标签</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>


    
  <div class="tags-list">
      <a href="/tag/外国文学">外国文学</a>
      <a href="/tag/言情">言情</a>
      <a href="/tag/美国">美国</a>
      <a href="/tag/文学">文学</a>
      <a href="/tag/爱情">爱情</a>
      <a href="/tag/中国">中国</a>
      <a href="/tag/中国文学">中国文学</a>
      <a href="/tag/英国">英国</a>
  </div>


  
  <form name="tsp_form" action="/tag/" method="GET">
    <input name="search_text" class="j a_search_text" type="text" size="24" maxlength="36" title="去其他标签" value=""/>
    <input class="butt" type="submit" value="进入"/>
  </form>
  <br/>
  <br/>


  <p class="pl2 mb30">
    &gt; <a href="/tag/">浏览全部图书标签</a>
  </p>


    <br/>
    <br/>
    
<div class="block5 movie_show">
    <h2>最近受关注的书-小说</h2>
    <div class="content clearfix" id="book_rec">
            <dl>
                <dt><a onclick="moreurl(this, {'r1001':'book-tag-top'})" 
                href="https://book.douban.com/subject/2230208/"><img src="https://img1.doubanio.com/spic/s2720819.jpg" 
                class="m_sub_img" /></a></dt>
                <dd><a onclick="moreurl(this, {'r1001':'book-tag-top'})"
                href="https://book.douban.com/subject/2230208/">我的前半生</a>
                </dd>
            </dl>
            <dl>
                <dt><a onclick="moreurl(this, {'r1001':'book-tag-top'})" 
                href="https://book.douban.com/subject/1003000/"><img src="https://img3.doubanio.com/spic/s9026255.jpg" 
                class="m_sub_img" /></a></dt>
                <dd><a onclick="moreurl(this, {'r1001':'book-tag-top'})"
                href="https://book.douban.com/subject/1003000/">悟空传</a>
                </dd>
            </dl>
            <dl>
                <dt><a onclick="moreurl(this, {'r1001':'book-tag-top'})" 
                href="https://book.douban.com/subject/25967870/"><img src="https://img1.doubanio.com/spic/s27432697.jpg" 
                class="m_sub_img" /></a></dt>
                <dd><a onclick="moreurl(this, {'r1001':'book-tag-top'})"
                href="https://book.douban.com/subject/25967870/">长白秘闻之不咸灵迹</a>
                </dd>
            </dl>
            <div class="clearfix rr" style="width:100%"></div>
            <dl>
                <dt><a onclick="moreurl(this, {'r1001':'book-tag-top'})" 
                href="https://book.douban.com/subject/27079142/"><img src="https://img1.doubanio.com/spic/s29484809.jpg" 
                class="m_sub_img" /></a></dt>
                <dd><a onclick="moreurl(this, {'r1001':'book-tag-top'})"
                href="https://book.douban.com/subject/27079142/">有匪3</a>
                </dd>
            </dl>
            <dl>
                <dt><a onclick="moreurl(this, {'r1001':'book-tag-top'})" 
                href="https://book.douban.com/subject/27006492/"><img src="https://img3.doubanio.com/spic/s29428074.jpg" 
                class="m_sub_img" /></a></dt>
                <dd><a onclick="moreurl(this, {'r1001':'book-tag-top'})"
                href="https://book.douban.com/subject/27006492/">戴上手套擦泪</a>
                </dd>
            </dl>
            <dl>
                <dt><a onclick="moreurl(this, {'r1001':'book-tag-top'})" 
                href="https://book.douban.com/subject/27064644/"><img src="https://img1.doubanio.com/spic/s29470789.jpg" 
                class="m_sub_img" /></a></dt>
                <dd><a onclick="moreurl(this, {'r1001':'book-tag-top'})"
                href="https://book.douban.com/subject/27064644/">北方大道</a>
                </dd>
            </dl>
            <div class="clearfix rr" style="width:100%"></div>
    </div>
</div>



  




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '42279477',
            browserId = 'PDswO7ExjHU',
            criteria = '3:/tag/小说?start=0&amp;type=T',
            preview = '',
            debug = false,
            adSlots = ['dale_book_tag_top_right'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/d59867ddbe8a25645584b467a58a41cbd672c9be/ad.release.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>











      </div>
      <div class="extra">
        
      </div>
    </div>
  </div>

        
  <div id="footer">
    
<span id="icp" class="fleft gray-link">
    &copy; 2005－2018 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>
    
    · <a href="https://help.douban.com/?app=book" target="_blank">帮助中心</a>
    · <a href="https://book.douban.com/library_invitation">图书馆合作</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

  </div>

    </div>
      
  

    <script type="text/javascript">
    $(function(){
      $('.add2cartWidget').each(function() {
        var add2CartBtn = $(this).find('.add2cart');
        var inCartHint = $(this).find('.book-in-cart');
        var deleteBtn = inCartHint.find('.delete-cart-item');

        deleteBtn.click(function(e) {
          e.preventDefault();
          $.post_withck('/cart', {remove: this.rel}, function() {
            add2CartBtn.show();
            inCartHint.hide();
          });
        });
      });
    });
  </script>
    <!-- mako -->
    
  <script>
    $(function () {
      function update_tags(current) {
        html = $.map(current, function(o) {return '<span class="tags-name">' + o + '</span><sup class="tags-del"></sup> '}).join('<span class="tags-add">+</span>');
        $('h1').html('<span class="name">电影标签：</span>' + html);
      };

      function get_current_tags() {
        var r = [];
        $('.tags-name').each(function() {r.push($(this).text())});
        return r;
      };

      function get_current_sort_type() {
        url = location.href;
        array = url.split("?")
        if (array.length == 1) {
          return "";
        }
        query = array[1];
        arr = query.split("&");
        for (var i = 0; i < arr.length; i++) {
          arr2 = arr[i].split('=');
          if (arr2[0] == "type") {
            if (arr2.length == 1) {
              return "";
            }
            return arr2[1];
          }
        }
        return "";
      };

      function update_subject_list(current, sort_type) {
        $('#subject_list').html('<span class="pl">载入中，请稍候...</span>');
        $('#subject_list').load_withck('/j/tag/j_subject_list', {tags:current.join(' '), type:sort_type}, function() {});
      };

      function update_related_tags_and_subject(current, sort_type) {
        update_related_tags(current, sort_type);
        // update_subject_list(current, sort_type);
      };

      function update_related_tags(current, sort_type) {
        $('#related_tags').load_withck('/j/tag/j_related_tag', {tags:current.join(' '), type:sort_type}, function() {
          $('.more').toggle(
            function () {
              $('.tags-hide').css('display', 'inline');
              $(this).text('收起▲');
            },
            function () {
              $('.tags-hide').hide();
              $(this).text('更多▼');
            }
          );
          $('.tags-del').click(function () {
            if($(this).prev().prev().text() == '+') {
              $(this).prev().prev().remove();
            } else if ($(this).next().text() == '+') {
              $(this).next().remove();
            }
            $(this).prev().remove().end().remove();
            current = get_current_tags();
            if (current.length == 0){
              document.location.href = '/tag/';
            } else {
              //setHash(current.join(' '));
              //location.href = '/tag/' + (location.href).split('#')[1] + '?type=' + sort_type;
              sort_type = get_current_sort_type();
              location.href = '/tag/' + current.join(' ') + '?type=' + sort_type;
            }
          });
          $('.add-tag').click(function () {
            current = get_current_tags();
            current.push($(this).text());
            update_tags(current);
            //setHash(current.join(' '));
            //location.href = '/tag/' + (location.href).split('#')[1] + '?type=' + sort_type;
            sort_type = get_current_sort_type();
            location.href = '/tag/' + current.join(' ') + '?type=' + sort_type;
          });
          $('.tagsInput').keypress(function (e) {
            if (e.which == 13) {
              current = get_current_tags();
              current.push($(this).val());
              update_tags(current);
              sort_type = get_current_sort_type();
              //setHash(current.join(' '));
              //location.href = '/tag/' + (location.href).split('#')[1] + '?type=' + sort_type;
              location.href = '/tag/' + current.join(' ') + '?type=' + sort_type;
            }
          });
          checkInput($('.tagsInput'));
        });
      };

      current = get_current_tags();
      sort_type = get_current_sort_type();
      update_related_tags_and_subject(current, sort_type);

      function checkInput (o) {
        if (!o.val() || o.val() == o.attr('title')) {
          o.addClass('greyinput');
          o.val(o.attr('title'));
        }
        o.focus(function(){
          o.removeClass('greyinput');
          if(o.val() == o.attr('title')) o.val('');
        });
        o.blur(function(){
          if(!o.val()){
            o.addClass('greyinput');
            o.val(o.attr('title'));
          }
        });
      }

      if($.browser.msie && $.browser.version == 6.0) {
        $('.tags-del').hover(
          function () { $(this).addClass('tags-hover'); },
          function () { $(this).removeClass('tags-hover'); }
        );
      }
      if (location.href.split('#').length > 1) {
        //changeUrl ();
      }

  });

  function setHash (a) {
    $.browser.msie?$.locationHash(a):location.hash = a;
  }
  </script>

    
  

<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; 
    g.type='text/javascript';
    g.defer=true; 
    g.async=true; 
    g.src=p+'://s.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
  })();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-16', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id])

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '1', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>








    <!-- sindar2b-docker-->

</body>
</html>






































"""
from Crawler.DouBan.DouBan.items import DoubanItem
import re

response_text = pq(html)
books = response_text.find('.subject-list .subject-item').items()
item = DoubanItem()
for book in books:
    item['cover'] = book.find('img').attr('src')
    item['name'] = book.find('h2 a').attr('title')
    item['url'] = book.find('h2 a').attr('href')
    pubs = book.find('.pub').text().split('/')
    item["author"] = pubs[0]
    item["translator"] = pubs[1] if len(pubs) == 5 else ' '
    item['press'] = pubs[len(pubs) - 3]
    item['publish_year'] = pubs[len(pubs) - 2]
    item['price'] = pubs[len(pubs) - 1]
    item['grade'] = book.find('.rating_nums').text()
    item["grade_count"] = re.search(r'(\d+)', book.find('.star.clearfix .pl').text()).group(0)
    item['content_synopsis'] = book.find('p').text()
    print(item)
