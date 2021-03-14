from bs4 import BeautifulSoup, Comment
# Loading the html page
soup = BeautifulSoup(open('../lesson_2_raw.html'), "html.parser")

# Remove all script (incomplete native mathjax config)
for s in soup.head.select('script'):
    s.extract()

# Remove all legacy style from the lesson
for s in soup.select('style'):
    s.extract()

# Remove comments
comments = soup.findAll(text=lambda text:isinstance(text, Comment))
for comment in comments:
   comment.extract()

# Insert Logo
icon = soup.new_tag("link")
icon.attrs["rel"] = "icon"
icon.attrs["href"] = "./resources/favicon.png"
soup.head.insert(4, icon)

# Insert the style sheets - css files
# legacy
nb_legacy = soup.new_tag("link")
nb_legacy.attrs["rel"] = "stylesheet"
nb_legacy.attrs["href"] = "./css/nbinteract_legacy.css"
soup.head.insert(6, nb_legacy)

# theme
theme = soup.new_tag("link")
theme.attrs["rel"] = "stylesheet"
theme.attrs["href"] = "./css/mooc_theme.css"
soup.head.insert(8, theme)

# font
font = soup.new_tag("link")
font.attrs["rel"] = "stylesheet"
font.attrs["href"] = "https://fonts.googleapis.com/css?family=Proxima+Nova"
soup.head.insert(10, font)

font_style = soup.new_tag("style")
soup.head.insert(12, font_style)
soup.head.style.append('body,h1,h2,h3,h4,h5 {font-family: "Proxima Nova", sans-serif}')

# Alter Title
soup.head.title.string = 'Lesson 2 - Irwin Failure Criteria and Fracture Toughness'

# Insert the mathjax script
mathjax = '''
            <!-- Scripts -->

            <!-- Loading mathjax macro -->
            <!-- Load mathjax -->
                <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
                <!-- MathJax configuration -->
                <script type="text/x-mathjax-config">
                MathJax.Hub.Config({
                  TeX: {
                    equationNumbers: { autoNumber: "AMS" },
                    tagSide: "right"
                  },
                    tex2jax: {
                        inlineMath: [ ['$','$'], ["\\\\(","\\\\)"] ],
                        displayMath: [ ['$$','$$'], ["\\\\[","\\\\]"] ],
                        processEscapes: true,
                        processEnvironments: true
                    },
                    // Center justify equations in code and markdown cells. Elsewhere
                    // we use CSS to left justify single line equations in code cells.
                    displayAlign: 'center',
                    "HTML-CSS": {
                        styles: {'.MathJax_Display': {"margin": 0}},
                        linebreaks: { automatic: true }
                    }
                });
                MathJax.Hub.Register.StartupHook("TeX AMSmath Ready", function () {
                MathJax.InputJax.TeX.Stack.Item.AMSarray.Augment({
                  clearTag() {
                    if (!this.global.notags) {
                      this.super(arguments).clearTag.call(this);
                    }
                  }
                });
              });
                </script>
                <!-- End of mathjax configuration -->
           '''
soup.head.append(BeautifulSoup(mathjax))

# Insert the menus script
menu_script = '''
                <script>
                 function overlayHelp(isShow){
                  var elm = document.getElementById('overlayHelp')
                  if (isShow) {
                    elm.style.display = 'block';
                  } else {
                    elm.style.display = 'none';
                  }
                }

                function openHelp() {
                  overlayHelp(true);
                  document.getElementById('HelpWindow').style.display = 'block';
                }

                function closeHelp() {
                  overlayHelp(false);
                  document.getElementById('HelpWindow').style.display = 'none';
                }

                function overlay(isShow){
                  var elm = document.getElementById('overlay')
                  if (isShow) {
                    elm.style.display = 'block';
                  } else {
                    elm.style.display = 'none';
                  }
                }

                function openNav() {
                  if (!e) var e = window.event;
                    e.cancelBubble = true;
                    if (e.stopPropagation) e.stopPropagation();
                  overlay(true);
                  // document.getElementById('mySidenav').style.width="250px";
                  document.getElementById('mySidenav').classList.add('sidenav_sz_open');
                  document.getElementById('mySidenav').classList.remove('sidenav_sz_close');
                  document.getElementById('sm_arrow').style.color="#222";
                  document.getElementById("notebook").style.marginLeft = "250px";
                  document.body.style.backgroundColor = "white";
                }

                function closeNav() {
                  if (!e) var e = window.event;
                    e.cancelBubble = true;
                    if (e.stopPropagation) e.stopPropagation();
                  overlay(false);
                  document.getElementById('mySidenav').classList.add('sidenav_sz_close');
                  document.getElementById('mySidenav').classList.remove('sidenav_sz_open');
                  document.getElementById("notebook").style.marginLeft = "0";
                  document.getElementById('sm_arrow').style.color="grey";
                  document.body.style.backgroundColor = "white";
                }

                function overlayIndex(isShow){
                  var elm = document.getElementById('overlayIndex')
                  if (isShow) {
                    elm.style.display = 'block';
                  } else {
                    elm.style.display = 'none';
                  }
                }

                function openIndex() {
                  if (!e) var e = window.event;
                      e.cancelBubble = true;
                    if (e.stopPropagation) e.stopPropagation();
                  overlayIndex(true);
                  document.getElementById('myIndex').classList.add('index_sz_open');
                  document.getElementById('myIndex').classList.remove('index_sz_close');
                }

                function closeIndex() {
                  if (!e) var e = window.event;
                      e.cancelBubble = true;
                    if (e.stopPropagation) e.stopPropagation();  
                  overlayIndex(false);
                  document.getElementById('myIndex').classList.add('index_sz_close');
                  document.getElementById('myIndex').classList.remove('index_sz_open');
                }
                </script>
           '''
soup.head.append(BeautifulSoup(menu_script))

# Menu Html
menu_html = '''
            <!-- Adding Logo -->
            <img class="logoGEMM" src="./resources/logo.png" width="80px">

            <!-- Navigation Bar -->
            <div class="topnav">
              <a class="active" href="index.html"><i class="fa fa-home"></i> Home</a>
              <a class="disabled"><i class="fa fa-arrow-left"></i>  Previous</a>
              <a href="#next">Next  <i class="fa fa-arrow-right"></i></a>
              <a href="#index" onclick="openIndex()"><i class="fa fa-list-ol"></i> Table of contents</a>
              <a class="feedback" href="./feedback.html"><i class="fa fa-comments"></i> Feedback</a>
              <a class="help" href="#help" onclick="openHelp()"><i class="fa fa-book"></i> Help</a>
            </div>

            <div id="myIndex" class="indexMenu index_sz_close">
                <br>
            <ul class="toc-item"><li><a href="#Overall-Properties-of-Ceramic-Materials" data-toc-modified-id="Overall-Properties-of-Ceramic-Materials-1" onclick="closeIndex();"><span class="toc-item-num">1&nbsp;&nbsp;</span>Overall Properties of Ceramic Materials</a></span><li><span><a href="#What-are-the-ceramic-properties-that-come-to-mind?" data-toc-modified-id="What-are-the-ceramic-properties-that-come-to-mind?-1.1" onclick="closeIndex();"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>What are the ceramic properties that come to mind?</a></span></li><li><span><a href="#Examples-of-Properties-of-Advanced-Ceramics" data-toc-modified-id="Examples-of-Properties-of-Advanced-Ceramics-1.2" onclick="closeIndex();"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Examples of Properties of <em>Advanced Ceramics</em></a></span><ul class="toc-item"><li><span><a href="#Ceramic-Ribbons" data-toc-modified-id="Ceramic-Ribbons-1.2.1" onclick="closeIndex();"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Ceramic Ribbons</a></span></li><li><span><a href="#Smartphone-Screens" data-toc-modified-id="Smartphone-Screens-1.2.2" onclick="closeIndex();"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Smartphone Screens</a></span></li><li><span><a href="#Space-Shuttle-Thermal-Tiles" data-toc-modified-id="Space-Shuttle-Thermal-Tiles-1.2.3" onclick="closeIndex();"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Space Shuttle Thermal Tiles</a></span></li><li><span><a href="#Important-Remarks:" data-toc-modified-id="Important-Remarks:-1.2.4" onclick="closeIndex();"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Important Remarks</a></span></li></ul></li><li><span><a href="#What-are-the-properties-that-define-the-mechanical-strength-of-the-ceramics?" data-toc-modified-id="What-are-the-properties-that-define-the-mechanical-strength-of-the-ceramics?-1.3" onclick="closeIndex();"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>What are the properties that define the mechanical strength of the ceramics?</a></span></li></li><li><span><a href="#How-strong-are-chemical-bonds?" data-toc-modified-id="How-strong-are-chemical-bonds?-2" onclick="closeIndex();"><span class="toc-item-num">2&nbsp;&nbsp;</span>How strong are chemical bonds?</a></span><ul class="toc-item"><li><span><a href="#Lennard-Jones-Model-for-Bonding-Energy" data-toc-modified-id="Lennard-Jones-Model-for-Bonding-Energy-2.1" onclick="closeIndex();"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Lennard-Jones Model for Bonding Energy</a></span></li></ul></li><li><span><a href="#Fracture-Energy" data-toc-modified-id="Fracture-Energy-3" onclick="closeIndex();"><span class="toc-item-num">3&nbsp;&nbsp;</span>Fracture Energy</a></span></li><li><span><a href="#Stress-Concentration-Factor" data-toc-modified-id="Stress-Concentration-Factor-4" onclick="closeIndex();"><span class="toc-item-num">4&nbsp;&nbsp;</span>Stress Concentration Factor</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5" onclick="closeIndex();"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></ul></div>
            </div>
            <div id="overlayIndex" onclick="closeIndex()"></div>


            <!-- Navigation Side Menu -->
            <div id="mySidenav" class="sidenav sidenav_sz_open" onclick="openNav()">
              <a id="sm_arrow" href="#" class="sm_arrow" >❯</a>
              <a><i class="fa fa-list"></i>  &nbsp;&nbsp; Index of Lessons</a>
              <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                  <ol>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_1.html'><b>Theoretical Stregth and Stress Concentrations</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_2.html'><b>Irwin Failure Criteria and Fracture Toughness</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_3.html'><b>Aluminum Oxide - Production, Phases, Properties and Selection</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_4.html'><b>Processing-Mechanical Properties of Ceramics Correlation</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_5.html'><b>The Grifth Failure Criterion</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_6.html'><b>Probability Applied to Ceramics - The Weibull Analysis</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_7.html'><b>Fracture Energy and Toughnening Mechanisms</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_8.html'><b>Examples of Toughening Mechanisms</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_9.html'><b>Subcritical Crack Propagation and Aplication to Bioceramics</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_10.html'><b>Thermal Shock - Concept and Evaluation</a></b></li>
              <li style='font-size: 14px; color:#818181; font-weight: bold'><a href='./lesson_11.html'><b>Unified Theory of Thermal Shock and Toughening Mechanisms Application</a></b></li>
            </ol>

            </div>

            <!-- Click anywhere to close -->
            <div id="overlay" onclick="closeNav()"></div>

            <!-- Help Menu -->
            <div id="overlayHelp" onclick="closeHelp()"></div>
            <div id="HelpWindow">
            <a href="javascript:void(0)" class="closebtnHelp" onclick="closeHelp()">&times;</a>
            <p>This MOOC is based on XX lessons. Each lesson is a webpage. You can go to the MOOC home by clicking the "Home" button. When available the next lesson can be found by clicking "Next". The previous lesson can be found in a similar manner. The side menu shows all the topics of the current lesson. On these lessons there are interactive widgets. They can be loaded by clicking in the following button:
            </p>
            <br>
            <div class="disabled_nbinteract_button">
                  Show widgets
            </div>
            <p><b>WARNING:</b> It can take up to 5 minutes to load everything.</p>
            <p>If you have any doubt or problems, please contact us:</p>
            <a href="mailto:moreira.murilo@gmail.com">Murilo Henrique Moreira</a>
            </div>
            '''
soup.head.append(BeautifulSoup(menu_html))

# Write the lesson to html
with open("../lesson_2.html", "w",  encoding="utf-8") as file:
    file.write(str(soup).replace('×', '&times;').replace('  ', '&nbsp;&nbsp;').replace('â†©', '↩'))
