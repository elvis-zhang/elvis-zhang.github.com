<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>坐下来思考 - 发现 传承 分享 - {{title}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="节约 传承 分享，二手书籍">
    <meta name="author" content="A Lucky Apple">

    <!-- Le styles -->
    <link href="/css/skin.css" rel="stylesheet">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="/ico/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/ico/apple-touch-icon-57-precomposed.png">
  </head>

  <body class="">
	<div class="header_holder header_bg">
    <div id="header">
		<div id="lanyizi_logo_main" class="float_left">
			<a href=""><img src="/img/lanyizi_main.png" alt="lanyizi_logo" /></a>
		</div>
		<div class="top_links_main">
			<a class="btn" href="/about.html">关于</a>
		</div>
    </div> <!-- /header -->
	</div> <!-- /header_holder -->
	<div class="bg_main bar_small"></div>
    <div class="bg_main">
		<div class="bar_small_i"></div>
		<div id="content_box">
			<div class="content_box_news" style="overflow:hidden">
				<div class="newsentry" style="">

					<div style="margin-top:20px;overflow:hidden">
						<div style="">
							<div class="newsentry_title">
							<a href="">{{title}}</a>
							</div>
					<div class="nesentryheader" style="height:11px;border-bottom:1px solid #E1E1E1;text-align:right;">
					<span style="display:inline-block;border-top:4px solid #E1E1E1;font-size:12px;color:#E1E1E1;position:relative;bottom:-11px;">{{post}}</span>
					</div>
							<div>
							{{content}}
							</div>
							<div style="font-size:12px;">
							分类:{{category_html}}
							标签:{{tag_html}}
							</div>
						</div>
					</div>
				</div>
				<div style="margin-top:10px;border-top:1px solid #e1e1e1;padding:10px 0;">
					<!-- UY BEGIN -->
					<div id="uyan_frame"></div>
					<script type="text/javascript" id="UYScript" src="http://v1.uyan.cc/js/iframe.js?UYUserId=1708067" async=""></script>
					<!-- UY END -->
				</div>
			</div>
			<div class="content_box_side">
				<div class="category">
					<h3>分类</h3>
					<ul id="category">
						<li>心情</li>
						<li>技术</li>
					</ul>
				</div>
				<div class="tag">
					<h3>标签</h3>
					<ul id="tag">
						<li>linux</li>
						<li>java</li>
					</ul>
				</div>
				<div class="archive">
					<h3>归档</h3>
					<ul id="archive">
						<li>2012-11(1)</li>
						<li>2012-12(1)</li>
					</ul>
				</div>
			</div>
		</div>

    </div> <!-- /container -->
	
    <div id="footer_no_border">
		<div class="bar_small_i"></div>
		<div class="footer_links">
			<a href="/about.html">关于蓝椅子</a>
			<a href="/acknowledge.html">致谢</a>
			<a href="/contact.html">联系作者</a>
		</div>
		<div class="footer_copyright">Copyright &copy; lanyizi.com 2012</div>
    </div> <!-- /footer -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery.js"></script>
  </body>
</html>
