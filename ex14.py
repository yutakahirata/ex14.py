'''
ex14.py ホームコントロール用ボタン
'''
from bottle import *
import json,os,requests
save=None
#color code
Color=[['lightsalmon', '#FFA07A', 'rgb(255,160,122)'] ,
['salmon', '#FA8072', 'rgb(250,128,114)'] ,
['darksalmon', '#E9967A', 'rgb(233,150,122)'] ,
['lightcoral', '#F08080', 'rgb(240,128,128)'] ,
['indianred', '#CD5C5C', 'rgb(205,92,92)'] ,
['crimson', '#DC143C', 'rgb(220,20,60)'] ,
['firebrick', '#B22222', 'rgb(178,34,34)'] ,
['red', '#FF0000', 'rgb(255,0,0)'] ,
['darkred', '#8B0000', 'rgb(139,0,0)'] ,
['coral', '#FF7F50', 'rgb(255,127,80)'] ,
['tomato', '#FF6347', 'rgb(255,99,71)'] ,
['orangered', '#FF4500', 'rgb(255,69,0)'] ,
['gold', '#FFD700', 'rgb(255,215,0)'] ,
['orange', '#FFA500', 'rgb(255,165,0)'] ,
['darkorange', '#FF8C00', 'rgb(255,140,0)'] ,
['lightyellow', '#FFFFE0', 'rgb(255,255,224)'] ,
['lemonchiffon', '#FFFACD', 'rgb(255,250,205)'] ,
['lightgoldenrodyellow', '#FAFAD2', 'rgb(250,250,210)'] ,
['papayawhip', '#FFEFD5', 'rgb(255,239,213)'] ,
['moccasin', '#FFE4B5', 'rgb(255,228,181)'] ,
['peachpuff', '#FFDAB9', 'rgb(255,218,185)'] ,
['palegoldenrod', '#EEE8AA', 'rgb(238,232,170)'] ,
['khaki', '#F0E68C', 'rgb(240,230,140)'] ,
['darkkhaki', '#BDB76B', 'rgb(189,183,107)'] ,
['yellow', '#FFFF00', 'rgb(255,255,0)'] ,
['lawngreen', '#7CFC00', 'rgb(124,252,0)'] ,
['chartreuse', '#7FFF00', 'rgb(127,255,0)'] ,
['limegreen', '#32CD32', 'rgb(50,205,50)'] ,
['lime', '#00FF00', 'rgb(0.255.0)'] ,
['forestgreen', '#228B22', 'rgb(34,139,34)'] ,
['green', '#008000', 'rgb(0,128,0)'] ,
['darkgreen', '#006400', 'rgb(0,100,0)'] ,
['greenyellow', '#ADFF2F', 'rgb(173,255,47)'] ,
['yellowgreen', '#9ACD32', 'rgb(154,205,50)'] ,
['springgreen', '#00FF7F', 'rgb(0,255,127)'] ,
['mediumspringgreen', '#00FA9A', 'rgb(0,250,154)'] ,
['lightgreen', '#90EE90', 'rgb(144,238,144)'] ,
['palegreen', '#98FB98', 'rgb(152,251,152)'] ,
['darkseagreen', '#8FBC8F', 'rgb(143,188,143)'] ,
['mediumseagreen', '#3CB371', 'rgb(60,179,113)'] ,
['seagreen', '#2E8B57', 'rgb(46,139,87)'] ,
['olive', '#808000', 'rgb(128,128,0)'] ,
['darkolivegreen', '#556B2F', 'rgb(85,107,47)'] ,
['olivedrab', '#6B8E23', 'rgb(107,142,35)'] ,
['lightcyan', '#E0FFFF', 'rgb(224,255,255)'] ,
['cyan', '#00FFFF', 'rgb(0,255,255)'] ,
['aqua', '#00FFFF', 'rgb(0,255,255)'] ,
['aquamarine', '#7FFFD4', 'rgb(127,255,212)'] ,
['mediumaquamarine', '#66CDAA', 'rgb(102,205,170)'] ,
['paleturquoise', '#AFEEEE', 'rgb(175,238,238)'] ,
['turquoise', '#40E0D0', 'rgb(64,224,208)'] ,
['mediumturquoise', '#48D1CC', 'rgb(72,209,204)'] ,
['darkturquoise', '#00CED1', 'rgb(0,206,209)'] ,
['lightseagreen', '#20B2AA', 'rgb(32,178,170)'] ,
['cadetblue', '#5F9EA0', 'rgb(95,158,160)'] ,
['darkcyan', '#008B8B', 'rgb(0,139,139)'] ,
['teal', '#008080', 'rgb(0,128,128)'] ,
['powderblue', '#B0E0E6', 'rgb(176,224,230)'] ,
['lightblue', '#ADD8E6', 'rgb(173,216,230)'] ,
['lightskyblue', '#87CEFA', 'rgb(135,206,250)'] ,
['skyblue', '#87CEEB', 'rgb(135,206,235)'] ,
['deepskyblue', '#00BFFF', 'rgb(0,191,255)'] ,
['lightsteelblue', '#B0C4DE', 'rgb(176,196,222)'] ,
['dodgerblue', '#1E90FF', 'rgb(30,144,255)'] ,
['cornflowerblue', '#6495ED', 'rgb(100,149,237)'] ,
['steelblue', '#4682B4', 'rgb(70,130,180)'] ,
['royalblue', '#4169E1', 'rgb(65,105,225)'] ,
['blue', '#0000FF', 'rgb(0,0,255)'] ,
['mediumblue', '#0000CD', 'rgb(0,0,205)'] ,
['darkblue', '#00008B', 'rgb(0,0,139)'] ,
['navy', '#000080', 'rgb(0,0,128)'] ,
['midnightblue', '#191970', 'rgb(25,25,112)'] ,
['mediumslateblue', '#7B68EE', 'rgb(123,104,238)'] ,
['slateblue', '#6A5ACD', 'rgb(106,90,205)'] ,
['darkslateblue', '#483D8B', 'rgb(72,61,139)'] ,
['lavender', '#E6E6FA', 'rgb(230,230,250)'] ,
['thistle', '#D8BFD8', 'rgb(216,191,216)'] ,
['plum', '#DDA0DD', 'rgb(221,160,221)'] ,
['violet', '#EE82EE', 'rgb(238,130,238)'] ,
['orchid', '#DA70D6', 'rgb(218,112,214)'] ,
['fuchsia', '#FF00FF', 'rgb(255,0,255)'] ,
['magenta', '#FF00FF', 'rgb(255,0,255)'] ,
['mediumorchid', '#BA55D3', 'rgb(186,85,211)'] ,
['mediumpurple', '#9370DB', 'rgb(147,112,219)'] ,
['blueviolet', '#8A2BE2', 'rgb(138,43,226)'] ,
['darkviolet', '#9400D3', 'rgb(148,0,211)'] ,
['darkorchid', '#9932CC', 'rgb(153,50,204)'] ,
['darkmagenta', '#8B008B', 'rgb(139,0,139)'] ,
['purple', '#800080', 'rgb(128,0,128)'] ,
['indigo', '#4B0082', 'rgb(75,0,130)'] ,
['pink', '#FFC0CB', 'rgb(255,192,203)'] ,
['lightpink', '#FFB6C1', 'rgb(255,182,193)'] ,
['hotpink', '#FF69B4', 'rgb(255,105,180)'] ,
['deeppink', '#FF1493', 'rgb(255,20,147)'] ,
['palevioletred', '#DB7093', 'rgb(219,112,147)'] ,
['mediumvioletred', '#C71585', 'rgb(199,21,133)'] ,
['white', '#FFFFFF', 'rgb(255,255,255)'] ,
['snow', '#FFFAFA', 'rgb(255,250,250)'] ,
['honeydew', '#F0FFF0', 'rgb(240,255,240)'] ,
['mintcream', '#F5FFFA', 'rgb(245,255,250)'] ,
['azure', '#F0FFFF', 'rgb(240,255,255)'] ,
['aliceblue', '#F0F8FF', 'rgb(240,248,255)'] ,
['ghostwhite', '#F8F8FF', 'rgb(248,248,255)'] ,
['whitesmoke', '#F5F5F5', 'rgb(245,245,245)'] ,
['seashell', '#FFF5EE', 'rgb(255,245,238)'] ,
['beige', '#F5F5DC', 'rgb(245,245,220)'] ,
['oldlace', '#FDF5E6', 'rgb(253,245,230)'] ,
['floralwhite', '#FFFAF0', 'rgb(255,250,240)'] ,
['ivory', '#FFFFF0', 'rgb(255,255,240)'] ,
['antiquewhite', '#FAEBD7', 'rgb(250,235,215)'] ,
['linen', '#FAF0E6', 'rgb(250,240,230)'] ,
['lavenderblush', '#FFF0F5', 'rgb(255,240,245)'] ,
['mistyrose', '#FFE4E1', 'rgb(255,228,225)'] ,
['gainsboro', '#DCDCDC', 'rgb(220,220,220)'] ,
['lightgray', '#D3D3D3', 'rgb(211,211,211)'] ,
['silver', '#C0C0C0', 'rgb(192,192,192)'] ,
['darkgray', '#A9A9A9', 'rgb(169,169,169)'] ,
['gray', '#808080', 'rgb(128,128,128)'] ,
['dimgray', '#696969', 'rgb(105,105,105)'] ,
['lightslategray', '#778899', 'rgb(119,136,153)'] ,
['slategray', '#708090', 'rgb(112,128,144)'] ,
['darkslategray', '#2F4F4F', 'rgb(47,79,79)'] ,
['black', '#000000', 'rgb(0,0,0)'] ,
['cornsilk', '#FFF8DC', 'rgb(255,248,220)'] ,
['blanchedalmond', '#FFEBCD', 'rgb(255,235,205)'] ,
['bisque', '#FFE4C4', 'rgb(255,228,196)'] ,
['navajowhite', '#FFDEAD', 'rgb(255,222,173)'] ,
['wheat', '#F5DEB3', 'rgb(245,222,179)'] ,
['burlywood', '#DEB887', 'rgb(222,184,135)'] ,
['tan', '#D2B48C', 'rgb(210,180,140)'] ,
['rosybrown', '#BC8F8F', 'rgb(188,143,143)'] ,
['sandybrown', '#F4A460', 'rgb(244,164,96)'] ,
['goldenrod', '#DAA520', 'rgb(218,165,32)'] ,
['peru', '#CD853F', 'rgb(205,133,63)'] ,
['chocolate', '#D2691E', 'rgb(210,105,30)'] ,
['saddlebrown', '#8B4513', 'rgb(139,69,19)'] ,
['sienna', '#A0522D', 'rgb(160,82,45)'] ,
['brown', '#A52A2A', 'rgb(165,42,42)'] ,
['maroon', '#800000', 'rgb(128,0,0)'] ,
]
#HTML デコレーション(Bootstrap4)
def Html(title,css=""):
    html='''
        <!DOCTYPE html>
            <html lang="ja">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
                <meta name="viewport" content = "width = device-width, initial-scale = 1.0, minimum-scale = 1, maximum-scale = 1, user-scalable = no" />
                <link rel="stylesheet" type="text/css" href="/static/content/MyBootatrp.css" />
	            <link href="static/content/jumbotron.css" rel="stylesheet" />
                <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
                <script src="/static/scripts/modernizr-2.6.2.js"></script>
                <script src="/static/scripts/jquery-1.10.2.min.js"></script>
                <script src="/static/scripts/bootstrap.min.js"></script>
                <script src="/static/scripts/respond.min.js"></script>
	            <script src="/static/scripts/mindmup-editabletable.js"></script>
                <script src="/static/scripts/jquery.redirect.js"></script>
            %s
            </head>
            <body><div style="margin-top:0.5em;">
            %s 
            </body></div>
            </html>'''
    def f0(f):
        def f1(*a,**b):          
            return html%(title,css,f(*a,**b))
        return f1
    return f0
def Body():
    def f0(f):
        def f1(*a,**b):
            return '<div class="container body-content">%s</div>'%f(*a,**b)
        return f1
    return f0
def Navi(menu):
    nav='''<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a class="navbar-brand" href="/">%s</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarsExampleDefault">
            <ul class="navbar-nav mr-auto">
                %s
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form>
            </div>
     </nav>%s'''
    def f0(f):
        def f1(*a,**b):
            nm=''.join(['<li class="nav-item"><a class="nav-link" href="/%s">%s</a></li>'%(x,x)
                       for x in menu[1:]])
            return nav%(menu[0],nm,f(*a,**b))
        return f1
    return f0
def routes(menu):
    def f0(f):
        route('/','GET',f)
        [route("/%s"%x,'GET',f) for x in menu]
        def f1(*a,**b):
            return f(*a,**b)
        return f1
    return f0
#JOMBOTRON デコレーション
def Jumbotron(title,paragraph):
    jumbo='''<div class="jumbotron">
        <div class="container">
          <h1 class="display-3">%s</h1>
          <p>%s</p>
        </div>
      </div>%s'''
    def f0(f):
        def f1(*a,**b):
            return jumbo%(title,paragraph,f(*a,**b))
        return f1
    return f0
#script デコレーション
def script(js):
    def f0(f):
        def f1(*a,**b):
            return f(*a,**b)+js
        return f1
    return f0
def style(css):
    def f0(f):
        def f1(*a,**b):
            return css+f(*a,**b)
        return f1
    return f0
js='''
<script>
$(function () {
    $('.btn').click(function(){
    $.get('/click/'+$(this).text(),{js:$(this).attr('id'),text:$(this).text()})
        .done(function(obj){
    
        });
    });
});
</script>'''
#Button デコレーション
def Button_(btn,clas,h='h1',id='id'):
    Hn="{0}"
    return "".join(["<button class='{0}' id='{3}{2}'>{1}</button>"
                    .format(clas,Hn.format(x),i,id) for i,x in enumerate(btn)])

def Button(btn,clas,h='h1',id='id'):
    bx=Button_(btn,clas,h,id)
    def f0(f):
        def f1(*a,**b):
            return bx+f(*a,**b)
        return f1
    return f0

menu='Home,bsz2,bsz3,bsz4,Help,color,round,rounded,rounded100,japan,ijapan,normal,tst,test,test1,test2,test3'.split(',')
css="<style>\n.w100{ width:100px; }\n%s</style>"%"".join(['.c%s { width:%spx; height:%spx; } \n'%(x,x,x) 
                                                          for x in range(100,400,50) ])
css1='''<style>
    .bsz2{width:137px;height:137px; font-size: small;}
    .bsz3{width:88px;height:88px;  font-size: small;} 
    .bsz4{width:64px;height:64px;  font-size: x-small;}
    .bsz2x{width:137px;height:66px; font-size: small;}
    .bsz2h{width:137px;height:33px; font-size: small;}
    .rounded-50 {border-radius: 0.50rem !important;}
    .rounded-100 {border-radius: 1rem !important;}
    .w136{width:136px;}
</style>
'''
@routes(menu)
@Html('HomeControl',css+css1)
@Navi(menu)
@Body()
@script(js)
def Home():
    global save
    btn="bsz4"
    p=request.urlparts[2]
    if p=='/color':
        return colorButton()
    elif p=='/round':
        return roundButton()
    elif p=='/rounded':
        return roundedButton()
    elif p=='/rounded100':
        return rounded100Button()    
    elif p=='/japan':
        return japanButton() 
    elif p=='/ijapan':
        return japanImgButton() 
    elif p=='/normal':
        return normalButton() 
    elif p=='/tst':
        return tstButton() 
    elif p=='/test':
        return testButton() 
    elif p=='/test1':
        return test1Button() 
    elif p=='/test2':
        return test2Button() 
    elif p=='/test3':
        return test3Button() 
    else:
        print(p,p[1:5])
        if p[1:4]=="bsz":
            btn=p[1:5]
        sz={'bsz2':6,'bsz3':12,'bsz4':20}
        lst=['B%s'%x for x in range(sz[btn])]
        b=Button_(lst,btn+' btn btn-primary m-1','h6','sw')
        return b

def colorButton():
    color='primary,secondary,success,danger,warning,info,light,dark'.split(',') 
    return "".join(["<button class='bsz3 btn btn-{0} m-1 ' id='id{1}'><h4>{2}</h4></button>"
                    .format(x,i,x.capitalize()) for i,x in enumerate(color)])
def roundButton():
    color='primary,secondary,success,danger,warning,info,light,dark'.split(',') 
    return "".join(["<button class='bsz2x btn btn-{0} rounded-pill m-1 ' id='id{1}'><h4>{2}</h4></button>"
                    .format(x,i,x.capitalize()) for i,x in enumerate(color)])
def roundedButton():
    color='primary,secondary,success,danger,warning,info,light,dark'.split(',') 
    return "".join(["<button class='bsz2x btn btn-{0} rounded-50 m-1 ' id='id{1}'><h4>{2}</h4></button>"
                    .format(x,i,x.capitalize()) for i,x in enumerate(color)])
def rounded100Button():
    color='primary,secondary,success,danger,warning,info,light,dark'.split(',') 
    return "".join(["<button class='bsz2x btn btn-{0} rounded-100 m-1 ' id='id{1}'><h4>{2}</h4></button>"
                    .format(x,i,x.capitalize()) for i,x in enumerate(color)])
def japanButton():
    color='primary,secondary,success,danger,warning,info,light,dark'.split(',') 
    return "".join(["<button class='bsz2 m-1'><img id ='jp{0}' src='/static/img/japan128.png'/>{0}</button>"
                    .format(i) for i in range(12)])
def japanImgButton():
    color='primary,secondary,success,danger,warning,info,light,dark'.split(',') 
    return "".join(["<img class='bsz2 btn p2' id ='jp{0}' src='/static/img/japan128.png'/>"
                    .format(i) for i in range(12)])
def normalButton():
    return "".join(["<input  type='button' value='Normal:{0}'/>"
                    .format(i) for i in range(12)])

def Join(s):
    return "".join(s);
def tstButton():
    return '''
    <style>
    .c{
        width:86px;
        height:86px;
        margin:1px;
        background: green;
        color:white;
        font-size:200%;
    }

    </style>'''+"".join(["<button class='c'>{0}</button>".format(x) for x in range(12) ])

def mkcss_btn(a,b):
    return '''
.btn-{0} {{
  color: #fff;
  background-color: {1};
  border-color: {1};
}}
.btn-{0}:hover {{
  color: #fff;
  background-color: #0069d9;
  border-color: #0062cc;
}}
.btn-{0}:focus, .btn-{0}.focus {{
  box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.5);
}}
.btn-{0}.disabled, .btn-{0}:disabled {{
  color: #fff;
  background-color: {1};
  border-color: {1};
}}
.btn-{0}:not(:disabled):not(.disabled):active, .btn-{0}:not(:disabled):not(.disabled).active,
.show > .btn-{0}.dropdown-toggle {{
  color: #fff;
  background-color: #0062cc;
  border-color: #005cbf;
}}
.btn-{0}:not(:disabled):not(.disabled):active:focus, .btn-{0}:not(:disabled):not(.disabled).active:focus,
.show > .btn-{0}.dropdown-toggle:focus {{
  box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.5);
}}
'''.format(a,b)
#print(mkcss_btn('gold','gold'))
css_btn="<style>\n"+Join([mkcss_btn(x[0],x[0]) for x in Color])+"\n</style>"
def testButton():
    print(len(Color))
    return Join(["<button class='bsz2h btn btn-success m-1' style='color:black;background:%s;'><b>%s</b></button>"%(x[0],x[0]) for x in Color])
def test1Button():
    return css_btn+Join(["<button class='bsz2h btn btn-{0} m-1'><b>{0}</b></button>".format(x[0]) for x in Color])
def test2Button():
    return Join(["<button class='bsz2h btn btn-{0} m-1'><b>{0}</b></button>".format(x[0]) for x in Color])
def test3Button():
    retval='<div class="d-inline-block p-5 bg-dark text-white">%s</div>'
    return retval%Join(["<button class='bsz2 btn btn-{0} m-1 rounded-pill'><h3><b>{0}</b></h3></button>".format(x) for x in 'gold,silver,bronze'.split(',')])
@route('/click/<name>')
def click(name):
    print(name)
#faviconの読み込み    
@route('/favicon.ico')
def favcon():
    return static_file('favicon.ico', root='./static')
#staic ファイルの読み込み
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')
#web server のhost portの設定
HOST,PORT='0.0.0.0',8080
if __name__ =='__main__':
    run(host=HOST,port=PORT)
