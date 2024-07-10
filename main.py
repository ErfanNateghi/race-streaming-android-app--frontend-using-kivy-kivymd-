from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from style import *

from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.uix.button import MDFloatingActionButton
from kivy.core.text import LabelBase


Window.size = (350,580)


KV = '''

# <Widget>:
#     font_name: 'F1_font'

#------------------------------------------------------------- login page
<LoginScreen>:
    MDCard:
        font_name: 'F1_font'
        focus_behavior: False
        size_hint: 0.85, 0.85
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 3
        shadow_color: app.theme_cls.primary_color
        padding: dp(10)
        spacing: dp(10)
        orientation: "vertical"
        BoxLayout:
            
            orientation: "vertical"
            Image:
                adaptive_height: True
                source: "mainlogo.png"
                size_hint: .6, .6
                pos_hint: {"center_x": .5}
                
            
            F1MDLabel:
                font_name: 'F1_font_bold'
                text: "Log In"
                text_color: (71/255,160/255,130/255,255/255)
                pos_hint: {"center_x": .5, "center_y": .5}
                font_size: sp(30)
                padding_y: dp(30)
                

            MDBoxLayout:
            
                font_name: 'F1_font'
                orientation: 'vertical'
                padding: dp(20)
                spacing: dp(20)
                MDTextField:
                    font_name: 'F1_font'
                    font_name_hint_text: 'F1_font'
                    id: username_input
                    hint_text: 'Username'
                    mode: "rectangle"
                    
                MDTextField:
                    font_name: 'F1_font'
                    id: password_input
                    hint_text: 'Password'
                    mode: "rectangle"
                    password: True
                MDGridLayout:
                    adaptive_height: True
                    rows:1
                    cols:4
                    spacing: dp(10)
                    
                    MDFlatButton:
                        font_name: 'F1_font'
                        text: ' Login '
                        on_release: app.root.get_screen('login_screen').do_login(username_input.text, password_input.text)
                        pos_hint: {"center_x": 0, "center_y": .5}
                        theme_text_color: "Custom"
                        text_color:(71/255,160/255,130/255,255/255)
                    Widget:
                    Widget:
                    MDFlatButton:
                        font_name: 'F1_font'
                        text: 'Sign Up'
                        pos_hint: {"center_x": 1, "center_y": .5}
                        theme_text_color: "Custom"
                        text_color:(71/255,160/255,130/255,255/255)
                MDRectangleFlatIconButton:
                    icon: "gmail"
                    text: "Log in with gmail"
                    font_name: 'F1_font'
                    pos_hint: {"center_x": .5, "center_y": .5}
                                  

#------------------------------------------------------------- main page       
<MainScreen>:
    MDBoxLayout:
        orientation: "vertical"
        

        MDTopAppBar:
            
            elevation: 3
            shadow_color: app.theme_cls.primary_color
            orientation:'horizontal'
            left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
            md_bg_color: [30/255,30/255,30/255,255/255]
            specific_text_color: (71/255,160/255,130/255,255/255)
            
            
            Image:
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                source:'small_logo.png'
                size_hint:None,None
                size: dp(150), dp(120)
            Widget:
            MDIconButton:
                icon:"face-man-profile"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:(0.05,0.05,0.05,1)
                
                
        
        BaseScreen:
            ScrollView:
                MDGridLayout:
                    
                    adaptive_height: True
                    cols:1
                    padding: dp(12)
                    spacing: dp(12)
                    
                    Widget:
                    MainpageCard:
                        height:dp(140)
                        on_press: app.on_chevron(card_1,0,f1_image) 
                        MDScreen:
                            id: card_1
                            FitImage:
                                id: f1_image
                                source: "f1.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(18), dp(18), dp(18), dp(18)
                                opacity: 1
                            
                                
                    Widget:  
                    MainpageCard:
                        height:dp(140)
                        on_press: app.on_chevron(card_2,1,wrc_image) 
                        MDScreen:
                            id: card_2
                            FitImage:
                                id: wrc_image
                                source: "wrc.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(18), dp(18), dp(18), dp(18)
                                opacity: 1
                    Widget:
                    MainpageCard:
                        height:dp(140)
                        on_press: app.on_chevron(card_3,2,dakar_image) 
                        MDScreen:
                            id: card_3
                            FitImage:
                                id: dakar_image
                                source: "dakar.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(18), dp(18), dp(18), dp(18)
                                opacity: 1
                    Widget:
                    MainpageCard:
                        height:dp(140)
                        on_press: app.on_chevron(card_4,3,wec_image) 
                        MDScreen:
                            id: card_4
                            FitImage:
                                id: wec_image
                                source: "wec.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(18), dp(18), dp(18), dp(18)
                                opacity: 1
                    Widget:
                    
                        
                        
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(8)
            padding: dp(8)
               
            MDList:
                OneLineIconListItem:
                    text: "[font=F1_font]Account[/font]"
                    IconLeftWidget:
                        icon: 'account'
                OneLineIconListItem:
                    text: "[font=F1_font]Notifications[/font]"
                    IconLeftWidget:
                        icon: 'bell'
                OneLineIconListItem:
                    text: "[font=F1_font]Auto Play[/font]"
                    IconLeftWidget:
                        icon: 'play'
                OneLineIconListItem:
                    text: "[font=F1_font]Watch on TV[/font]"
                    IconLeftWidget:
                        icon: 'television'
                OneLineIconListItem:
                    text: "[font=F1_font]Downloads[/font]"
                    IconLeftWidget:
                        icon: 'download'
                OneLineIconListItem:
                    text: "[font=F1_font]Accessibility[/font]"
                    IconLeftWidget:
                        icon: 'human'
                OneLineIconListItem:
                    text: "[font=F1_font]About[/font]"
                    IconLeftWidget:
                        icon: 'information'
                    
            Widget:
                        
#------------------------------------------------------------- stream page
<StreamPage>:

    ScrollView:
        MDGridLayout:
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            cols:1
            StreamPageTopAppBar:
                orientation:'horizontal'
                left_action_items: [["arrow-u-left-top-bold", lambda x: app.back()],["face-man-profile", ]]
                md_bg_color: [50/255,50/255,50/255,255/255]
                specific_text_color: (240/255,46/255,14/255,255/255)
                elevation: 5
                Image:
                    markup: True
                    size_hint_x: None
                    size: dp(48), dp(48)
                    pos_hint: {'center_x': 0.5}
                    source:'car.png'
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 1, None
                height: dp(250)
                VideoPlayer:
                    source: 'f1.mkv'
                    thumbnail:'f1_thumbnail.jpg'
                    height:dp(250)
                    size_hint: 1, None
                    
                
            StreamPageCard:
                on_press: app.go_to_minor_pages('f1_team_detail')
                FitImage:
                    source: "f1_team_detail.png"
                    size_hint_y: 1
                    pos_hint: {"top": 1}
                    radius: dp(50), dp(50), dp(50), dp(50)
                    opacity: 1
            StreamPageCard:
                
                on_press: app.go_to_minor_pages('f1_drivers')
                FitImage:
                    source: "f1_driver_status.png"
                    size_hint_y: 1
                    pos_hint: {"top": 1}
                    radius: dp(50), dp(50), dp(50), dp(50)
                    opacity: 1
            StreamPageCard:
                
                on_press: app.go_to_minor_pages('f1_track_details')
                FitImage:
                    source: "f1_track_details.png"
                    size_hint_y: 1
                    pos_hint: {"top": 1}
                    radius: dp(50), dp(50), dp(50), dp(50)
                    opacity: 1
            StreamPageCard:
                height:dp(412)
                padding: dp(6)
                StreamPageCard:
                    height:dp(400)
                    adaptive_height: True
                    md_bg_color:(39/255,60/255,77/255,255/255)
                    F1MDLabel:
                        font_name: 'F1_font_bold'
                        text: "GRID"
                        font_size: sp(30)
                        padding_y: dp(20)
                        
                    MDList:
                        adaptive_height: True
                        padding: dp(10), dp(10), dp(10), dp(10)
                        spacing: dp(10)
                        StreamPageCard:
                            on_press: app.go_to_minor_pages('f1_drivers')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_grid_1.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                                opacity: 1
                        StreamPageCard:
                            on_press: app.go_to_minor_pages('f1_drivers')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_grid_2.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                                opacity: 1
                        StreamPageCard:
                            on_press: app.go_to_minor_pages('f1_drivers')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_grid_3.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                                opacity: 1
                        StreamPageCard:
                            on_press: app.go_to_minor_pages('f1_drivers')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_grid_4.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                                opacity: 1
                        StreamPageCard:
                            on_press: app.go_to_minor_pages('f1_drivers')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_grid_5.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                                opacity: 1
                        StreamPageCard:
                            on_press: app.go_to_minor_pages('f1_drivers')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_grid_6.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                                opacity: 1
                    Widget:


#-------------------------------------------------------------  team detail screen                 
<F1TeamDetailsScreen>:
    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            MDFloatingActionButton:
                icon:'arrow-down-bold'
                on_release: app.back_to_racepage('streampage_f1')
                pos_hint:{"center_x": .5, "center_y": .5}
            StreamPageCard:
                height:dp(490)
                adaptive_height: True
                padding: dp(6)
                StreamPageCard:
                    height:dp(480)
                    adaptive_height: True
                    md_bg_color:(39/255,60/255,77/255,255/255)
                    F1MDLabel:
                        font_name: 'F1_font_bold'
                        text: "TEAMS"
                        font_size: sp(30)
                        padding_y: dp(20)
                        
                    MDList:
                        adaptive_height: True
                        padding: dp(10), dp(10), dp(10), dp(10)
                        spacing: dp(10)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('team_f1_1')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_team_1.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                        StreamPageCard:
                            #on_release: app.go_to_minor_pages('team_f1_1')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_team_2.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                        StreamPageCard:
                            #on_release: app.go_to_minor_pages('team_f1_1')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_team_3.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                        StreamPageCard:
                            #on_release: app.go_to_minor_pages('team_f1_1')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_team_4.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                        StreamPageCard:
                            #on_release: app.go_to_minor_pages('team_f1_1')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_team_5.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                        StreamPageCard:
                            #on_release: app.go_to_minor_pages('team_f1_1')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_team_6.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                        StreamPageCard:
                            #on_release: app.go_to_minor_pages('team_f1_1')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_team_7.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                        StreamPageCard:
                            #on_release: app.go_to_minor_pages('team_f1_1')
                            height:dp(35)
                            radius: dp(10), dp(10), dp(10), dp(10)
                            FitImage:
                                source: "f1_team_8.png"
                                size_hint_y: 1
                                pos_hint: {"top": 1}
                                radius: dp(10), dp(10), dp(10), dp(10)
                        
                    Widget:       
                
#------------------------------------------------------------- 
<Team_f1_1_screen>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('f1_team_detail')
                    pos_hint:{"center_x": .5, "center_y": .5}
                

            StreamPageCard:
                adaptive_height: True
                radius: dp(55)
                height:dp(100)
                FitImage:
                    source: "f1_aston_martin.png"
                    size_hint_y: 1
                    pos_hint: {"top": 1}
                    radius: dp(55)
            MDGridLayout:
                cols:1
                adaptive_height: True
                padding: dp(1)
                spacing: dp(1)
                StreamPageCard:
                    radius: dp(55),dp(55),0,0
                    md_bg_color:(2/255,45/255,38/255,255/255)#(3/255,74/255,63/255,255/255)
                    height:dp(300)
                    padding:dp(20)
                    F1MDLabel:
                        font_name: 'F1_font'
                        text: "The culmination of countless hours of work and uncompromising craft, the AMRZ4 builds on the strengths of its predecessor and applies the learnings from our most successful season to date. "
                    F1MDLabel:
                        font_name: 'F1_font'
                        text: "DRIVER: Fernando Alonso"
                    F1MDLabel:
                        text: "ENGINE: MercedeAMG "
                        theme_text_color: "Custom"
                    F1MDLabel:
                        text: "POINTS: 125"
                        text_color: 'orange'
                        font_size: sp(25)
                        padding_y: dp(30)

                    Widget:

                StreamPageCard:
                    radius: 0,0,0,0
                    md_bg_color:(2/255,45/255,38/255,255/255)
                    height:dp(330)
                    F1MDLabel:
                        font_name: 'F1_font_bold'
                        text: "DRIVERS"
                        font_size: sp(25)
                        padding_y: dp(30)
                    StreamPageCard:
                        md_bg_color:(2/255,45/255,38/255,255/255)
                        FitImage:
                            source: "f1_aston_martin_team.png"
                    Widget:
                StreamPageCard:
                    radius: 0,0,dp(55),dp(55)
                    md_bg_color:(2/255,45/255,38/255,255/255)
                    height:dp(250)

                    F1MDLabel:
                        font_name: 'F1_font_bold'
                        text: "GALLERY"
                        font_size: sp(25)
                    StreamPageCard:
                        padding:dp(20)
                        md_bg_color:(2/255,45/255,38/255,255/255)
                        FitImage:
                            source: "f1_team_gallery1.png"
                            size_hint: 1,1
                            radius:dp(10)
                            
                    Widget:    
                    
            Widget:
#-------------------------------------------------------------                
<F1DriversScreen>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('streampage_f1')
                    pos_hint:{"center_x": .5, "center_y": .5}
                

            StreamPageCard:
                adaptive_height: True
                radius: dp(55)
                height:dp(100)
                FitImage:
                    source: "f1_fernando1.png"
                    size_hint_y: 1
                    pos_hint: {"top": 1}
                    radius: dp(55)
            MDGridLayout:
                cols:1
                adaptive_height: True
                padding: dp(1)
                spacing: dp(1)
                StreamPageCard:
                    radius: dp(55),dp(55),0,0
                    height:dp(450)
                    FitImage:
                        source: "f1_fernando2.png"
                        size_hint:1,1
                        pos_hint: {"top": 1}
                        radius: dp(55),dp(55),0,0
                        
                StreamPageCard:
                    radius: 0,0,0,0
                    height:dp(330)
                    FitImage:
                        source: "f1_fernando3.png"
                        size_hint:1,1
                        
                StreamPageCard:
                    radius: 0,0,dp(55),dp(55)
                    height:dp(300)
                    md_bg_color:(0/255,18/255,14/255,255/255)
                    F1MDLabel:
                        font_name: 'F1_font_bold'
                        text: "GALLERY"
                        font_size: sp(25)
                    StreamPageCard:
                        padding:dp(10)
                        spacing:dp(10)
                        md_bg_color:(0/255,18/255,14/255,255/255)
                        height: dp(200)
                        FitImage:
                            source: "f1_fernando4.png"
                            size_hint:.9,.9
                            pos_hint: {"center_x": .5, "center_y": .5}
                            radius:dp(10)
                    Widget:
                        

            Widget:
#------------------------------------------------------------- 
<F1TrackDetailsScreen>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('streampage_f1')
                    pos_hint:{"center_x": .5, "center_y": .5}
            

            MDGridLayout:
                cols:1
                adaptive_height: True
                padding: dp(1)
                spacing: dp(1)
                StreamPageCard:
                    radius: dp(55),dp(55),0,0
                    height:dp(550)
                    padding: dp(5)
                    FitImage:
                        source: "f1_track_detail.png"
                        size_hint:1,1
                        pos_hint: {"top": 1}
                        radius: dp(55),dp(55),0,0
                        
                StreamPageCard:
                    radius: 0,0,dp(55),dp(55)
                    height:dp(700)
                    md_bg_color:(25/255,39/255,50/255,255/255)
                    F1MDLabel:
                        font_name: 'F1_font_bold'
                        text: "GALLERY"
                        font_size: sp(25)
                    StreamPageCard:
                        padding:dp(10)
                        spacing:dp(10)
                        md_bg_color:(25/255,39/255,50/255,255/255)
                        height: dp(600)

                        FitImage:
                            source: "f1_track_gallery1.png"
                            size_hint:.9,.9
                            pos_hint: {"center_x": .5, "center_y": .5}
                            radius:dp(10)
                        FitImage:
                            source: "f1_track_gallery2.png"
                            size_hint:.9,.9
                            pos_hint: {"center_x": .5, "center_y": .5}
                            radius:dp(10)
                        FitImage:
                            source: "f1_track_gallery3.png"
                            size_hint:.9,.9
                            pos_hint: {"center_x": .5, "center_y": .5}
                            radius:dp(10)
                            

                    Widget:


#------------------------------------------------------------- wrc page
<Wrc_screen>:
    ScrollView:
        MDGridLayout:
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            cols:1
            StreamPageTopAppBar:
                orientation:'horizontal'
                left_action_items: [["arrow-u-left-top-bold", lambda x: app.back()],["face-man-profile", ]]
                md_bg_color: [50/255,50/255,50/255,255/255]
                specific_text_color: (18/255,17/255,11/255,255/255)
                elevation: 5
                Image:
                    markup: True
                    size_hint_x: None
                    size: dp(100), dp(48)
                    pos_hint: {'center_x': 0.5}
                    source:'wrc_logo.png'
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 1, None
                height: dp(200)
                VideoPlayer:
                    source: 'wrc.mkv'
                    #options: {'eos': 'loop'}
                    height:dp(200)
                    size_hint: 1, None
                    
                
                # MyVideoPlayer:
                #     source: 'testvideo.mkv'
                #     state: 'play'
                #     options: {'eos': 'loop'}
                #     show_controls: False
                #     on_touch_down: if self.collide_point(*args[1].pos): self.show_controls = not self.show_controls
                    

            StreamPageCard:
                height:dp(500)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(39/255,60/255,77/255,255/255)
                    height:dp(490)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "MANUFACTURES"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_manufacturers')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_manufacture_1.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_manufacturers')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_manufacture_2.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_manufacturers')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_manufacture_3.png"
                                size_hint_y: 1
                                radius: dp(20)
                        Widget:
            StreamPageCard:
                on_press: app.go_to_minor_pages('wrc_track_details')
                FitImage:
                    source: "wrc_track_details.png"
                    size_hint_y: 1
                    pos_hint: {"top": 1}
                    radius: dp(50)
                    opacity: 1
            StreamPageCard:
                height:dp(500)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(39/255,60/255,77/255,255/255)
                    height:dp(490)
                    MDGridLayout:
                        cols:1
                        
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "DRIVERS"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_drivers')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_driver3.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_drivers')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_driver3.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_drivers')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_driver3.png"
                                size_hint_y: 1
                                radius: dp(20)
                        Widget:

#------------------------------------------------------------- 
<Wrc_manufacturers>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('streampage_wrc')
                    pos_hint:{"center_x": .5, "center_y": .5}
            

            MDGridLayout:
                cols:1
                adaptive_height: True
                padding: dp(1)
                spacing: dp(1)
                StreamPageCard:
                    radius: dp(55)
                    height:dp(600)
                    padding: dp(5)
                    FitImage:
                        source: "wrc_manufacturers.png"
                        size_hint:1,1
                        pos_hint: {"top": 1}
                        radius: dp(55)





#------------------------------------------------------------- 
<Wrc_drivers>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('streampage_wrc')
                    pos_hint:{"center_x": .5, "center_y": .5}
            

            MDGridLayout:
                cols:1
                adaptive_height: True
                padding: dp(1)
                spacing: dp(1)
                StreamPageCard:
                    radius: dp(55)
                    height:dp(600)
                    padding: dp(5)
                    FitImage:
                        source: "wrc_drivers.png"
                        size_hint:1,1
                        pos_hint: {"top": 1}
                        radius: dp(55)



#------------------------------------------------------------- 
<Wrc_trackdetails>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('streampage_wrc')
                    pos_hint:{"center_x": .5, "center_y": .5}
            
            StreamPageCard:
                height:dp(530)
                padding:dp(5)

                MDGridLayout:
                    cols:1
                    adaptive_height: True
                    StreamPageCard:
                        md_bg_color:(39/255,60/255,77/255,255/255)
                        radius: dp(55),dp(55),0,0
                        height:dp(180)
                        padding: dp(5)
                        FitImage:
                            source: "wrc_trackdetail_card1.png"
                            size_hint:1,1
                            pos_hint: {"top": 1}
                            radius: dp(55),dp(55),0,0
                    StreamPageCard:
                        md_bg_color:(39/255,60/255,77/255,255/255)
                        radius: 0
                        height:dp(200)
                        padding: dp(5)
                        on_release: app.go_to_minor_pages('wrc_stages')
                        FitImage:
                            source: "wrc_trackdetail_card2.png"
                            size_hint:1,1
                            pos_hint: {"top": 1}
                            radius: dp(55)
                    StreamPageCard:
                        md_bg_color:(39/255,60/255,77/255,255/255)
                        radius: 0,0,dp(55),dp(55)
                        height:dp(140)
                        padding: dp(5)
                        on_release: app.go_to_minor_pages('wrc_stages')
                        FitImage:
                            source: "wrc_trackdetail_card3.png"
                            size_hint:1,1
                            pos_hint: {"top": 1}
                            radius: dp(55)

#------------------------------------------------------------- 
<Wrc_stages>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('wrc_track_details')
                    pos_hint:{"center_x": .5, "center_y": .5}
            
            StreamPageCard:
                height:dp(450)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(39/255,60/255,77/255,255/255)
                    height:dp(440)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "STAGES"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_stage_1')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_stage1.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_stage_1')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_stage2.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('wrc_stage_1')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_stage3.png"
                                size_hint_y: 1
                                radius: dp(20)
                        

#------------------------------------------------------------- 
<Wrc_stage_1>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('wrc_stages')
                    pos_hint:{"center_x": .5, "center_y": .5}
            
            StreamPageCard:
                height:dp(500)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(39/255,60/255,77/255,255/255)
                    height:dp(490)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "STAGE 1"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            height:dp(200)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_stage1_text.png"
                                size_hint_y: 1
                                radius: dp(20)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "GALLERY"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_stage1_gallery1.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            height:dp(50)
                            radius: dp(20)
                            FitImage:
                                source: "wrc_stage1_gallery2.png"
                                size_hint_y: 1
                                radius: dp(20)

#------------------------------------------------------------- 
<Dakar_screen>:
    ScrollView:
        MDGridLayout:
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            cols:1
            StreamPageTopAppBar:
                orientation:'horizontal'
                left_action_items: [["arrow-u-left-top-bold", lambda x: app.back()],["face-man-profile", ]]
                md_bg_color: [50/255,50/255,50/255,255/255]
                specific_text_color: (1,1,1,255/255)
                elevation: 5
                Image:
                    markup: True
                    size_hint_x: None
                    size: dp(100), dp(48)
                    pos_hint: {'center_x': 0.5}
                    source:'dakar_logo.png'
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 1, None
                height: dp(200)
                VideoPlayer:
                    source: 'dakar.mkv'
                    #options: {'eos': 'loop'}
                    height:dp(200)
                    size_hint: 1, None
                    allow_stretch:True
            StreamPageCard:
                height:dp(450)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(30/255,50/255,67/255,255/255)
                    height:dp(440)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "CLASSIFICATION"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_classification_bike.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_classification_car.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_classification_truck.png"
                                size_hint_y: 1
                                radius: dp(20)
                        Widget:

                        
            StreamPageCard:
                height:dp(560)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(30/255,50/255,67/255,255/255)
                    height:dp(550)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "ROUTE"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            md_bg_color:(30/255,50/255,77/255,255/255)
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(260)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_route1.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(90)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_route2.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(90)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_route3.png"
                                size_hint_y: 1
                                radius: dp(20)
                        Widget:
            StreamPageCard:
                height:dp(1650)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(30/255,50/255,67/255,255/255)
                    height:dp(1640)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "COMPETITORS"
                            halign: 'center'
                            font_size: sp(25)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "BIKE"
                            halign: 'center'
                            font_size: sp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors1.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors2.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors3.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors4.png"
                                size_hint_y: 1
                                radius: dp(20)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "CAR"
                            halign: 'center'
                            font_size: sp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors5.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors6.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors7.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors8.png"
                                size_hint_y: 1
                                radius: dp(20)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "TRUCK"
                            halign: 'center'
                            font_size: sp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors9.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors10.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors11.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "dakar_competitors12.png"
                                size_hint_y: 1
                                radius: dp(20)
                        Widget:
                


#------------------------------------------------------------- wec page
<Wec_screen>:
    ScrollView:
        MDGridLayout:
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            cols:1
            StreamPageTopAppBar:
                orientation:'horizontal'
                left_action_items: [["arrow-u-left-top-bold", lambda x: app.back()],["face-man-profile", ]]
                md_bg_color: [50/255,50/255,50/255,255/255]
                specific_text_color: (14/255,37/255,69/255,255/255)
                elevation: 5
                Image:
                    markup: True
                    size_hint_x: None
                    size: dp(100), dp(48)
                    pos_hint: {'center_x': 0.5}
                    source:'wec_logo.png'
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 1, None
                height: dp(200)
                VideoPlayer:
                    source: 'wac.mkv'
                    #options: {'eos': 'loop'}
                    height:dp(200)
                    size_hint: 1, None
                    allow_stretch:True
            StreamPageCard:
                height:dp(380)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(30/255,50/255,67/255,255/255)
                    height:dp(370)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "CLASSIFICATION"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(130)
                            radius: dp(20)
                            FitImage:
                                source: "wec_classification1.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(130)
                            radius: dp(20)
                            FitImage:
                                source: "wec_classification2.png"
                                size_hint_y: 1
                                radius: dp(20)
                        Widget:

            StreamPageCard:
                height:dp(1200)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(30/255,50/255,67/255,255/255)
                    height:dp(1190)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "COMPETITORS"
                            halign: 'center'
                            font_size: sp(25)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "HYPERCAR"
                            halign: 'center'
                            font_size: sp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wec_competitors1.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wec_competitors2.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wec_competitors3.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wec_competitors4.png"
                                size_hint_y: 1
                                radius: dp(20)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "LMPGT3"
                            halign: 'center'
                            font_size: sp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wec_competitors5.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wec_competitors6.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wec_competitors7.png"
                                size_hint_y: 1
                                radius: dp(20)
                        StreamPageCard:
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(110)
                            radius: dp(20)
                            FitImage:
                                source: "wec_competitors8.png"
                                size_hint_y: 1
                                radius: dp(20)
                        
                        Widget:
            StreamPageCard:
                height:dp(600)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(30/255,50/255,67/255,255/255)
                    height:dp(590)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "TRACK DETAILS"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            md_bg_color:(30/255,50/255,77/255,255/255)
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(500)
                            radius: dp(20)
                            FitImage:
                                source: "wec_track.png"
                                size_hint_y: 1
                                radius: dp(20)
                        Widget:

            StreamPageCard:
                height:dp(600)
                padding:dp(5)

                StreamPageCard:
                    md_bg_color:(30/255,50/255,67/255,255/255)
                    height:dp(590)
                    MDGridLayout:
                        cols:1
                        padding: dp(12)
                        spacing: dp(12)
                        MDLabel:
                            font_name: 'F1_font_bold'
                            text: "TIMES"
                            halign: 'center'
                            font_size: sp(25)
                        StreamPageCard:
                            md_bg_color:(30/255,50/255,77/255,255/255)
                            on_release: app.go_to_minor_pages('demo_screen')
                            height:dp(500)
                            radius: dp(20)
                            FitImage:
                                source: "wec_times.png"
                                size_hint_y: 1
                                radius: dp(20)
                        Widget:        
                


#------------------------------------------------------------- 
<BaseScreen>

<Demo_screen>:
    ScrollView:
        MDGridLayout:
            cols:1
            adaptive_height: True
            padding: dp(12)
            spacing: dp(12)
            StreamPageCard:
                MDLabel:
                    font_name: 'F1_font_bold'
                    text: "This Is The Demo Application"
                    halign: 'center'
                    font_size: sp(25)
                    padding: dp(5)
                MDLabel:
                    font_name: 'F1_font'
                    text: "tap the button below to go back to the main page"
                    halign: 'center'
                    font_size: sp(18)
                    padding: dp(5)

            StreamPageCard:
                md_bg_color:(18/255,18/255,18/255,255/255)
                height: dp(60)
                MDFloatingActionButton:
                    adaptive_height: True
                    icon:'arrow-down-bold'
                    on_release: app.back_to_racepage('main_screen')
                    pos_hint:{"center_x": .5, "center_y": .5}

<Box>:
    orientation: "vertical"
    size_hint_y: None
    height: self.minimum_height
    pos_hint: {"center_x": .5, "center_y": .5}

<MainpageCard>:
    size_hint: 1, None
    orientation: "vertical"
    elevation: 4
    shadow_color: app.theme_cls.primary_color
    pos_hint: {"center_x": .5, "center_y": .5}
    radius: dp(18)
<StreamPageCard>:
    size_hint: 1, None
    orientation: "vertical"
    pos_hint: {"center_x": .5, "center_y": .5}
    radius: dp(50), dp(50), dp(50), dp(50)
    height:dp(180)
<StreamPageTopAppBar>:
    radius: dp(50), dp(50), dp(50), dp(50)
<F1MDLabel>:
    adaptive_height: True
    font_name: 'F1_font'
    theme_text_color: "Custom"
    text_color: 'white'
    halign: "center"
    pos_hint: {"center_x": .5, "center_y": .5}
    font_size: sp(14)
    size_hint_y: None
    padding_y: dp(10)
#-------------------------------------------------------------     
#-----------------------------------------------------------------------------------------------------------------------------
MDScreenManager:
    id: screen_manager
    name: 'screen_manager'

    #--------------------

    LoginScreen:
        id: login_screen
        name: 'login_screen'

    #--------------------

    MainScreen:
        id: main_screen
        name: 'main_screen'

    #--------------------   

    StreamPage:
        id: streampage_f1
        name: 'streampage_f1'
        
    Wrc_screen:
        id: streampage_wrc
        name: 'streampage_wrc'    
        
    Dakar_screen:
        id: streampage_dakar
        name: 'streampage_dakar'

    Wec_screen:
        id: streampage_wec
        name: 'streampage_wec'
    
    #--------------------
    F1TeamDetailsScreen:
        id: f1_team_detail
        name: 'f1_team_detail'
    Team_f1_1_screen:
        id: team_f1_1
        name: 'team_f1_1'
    
    F1DriversScreen:
        id: f1_drivers
        name: 'f1_drivers'

    F1TrackDetailsScreen:
        id: f1_track_details
        name: 'f1_track_details'
    #--------------------
    Wrc_manufacturers:
        id: wrc_manufacturers
        name: 'wrc_manufacturers'
    
    Wrc_drivers:
        id: wrc_drivers
        name: 'wrc_drivers'

    Wrc_trackdetails:
        id: wrc_track_details
        name: 'wrc_track_details'

    Wrc_stages:
        id: wrc_stages
        name: 'wrc_stages'

    Wrc_stage_1:
        id: wrc_stage_1
        name: 'wrc_stage_1'    
    #--------------------
    
    Demo_screen:
        id: demo_screen
        name: 'demo_screen'
'''


#-----------------------------------------------------------------------------------------------------------------------------

class RacingApp(MDApp):
    
    def on_chevron(self,card_layout,id_number,hover_image):
        self.is_expanded[id_number] = not self.is_expanded[id_number]
        
        if self.is_expanded[id_number]:
            self.animation_card_hover(hover_image)
            self.item[id_number] = Box()
            labels = []
            l = self.playicons[id_number]
            self.item[id_number].add_widget(l)
            labels.append(l)
            card_layout.add_widget(self.item[id_number])
            self.animate_labels(labels)
            
        else:
            card_layout.remove_widget(card_layout.children[0])
            Animation(duration=0.5,opacity= 1).start(hover_image)
            self.item[id_number].remove_widget(self.item[id_number].children[0])
       
    def animate_labels(self, labels):
        anims = []
        for i in range(len(labels)+1):
            anims.append(Animation( font_size=15,duration=0.5,t='in_quad',opacity= 1))
        for i in range(len(labels)):
            anims[i].start(labels[i]) 
    
    def animation_card_hover(self, image):
        Animation(duration=0.5,opacity= 0.5).start(image)

    def mainpage_to_streampage(self, item_text):
        self.root.transition.direction = "left"
        self.root.current = item_text

    def back(self):
        self.root.transition.direction = "right"
        self.root.current = 'main_screen'
        
    def back_to_racepage(self,item_text):
        self.root.transition.direction = "down"
        self.root.current = item_text    
        
    def go_to_minor_pages(self, item_text):
        self.root.transition.direction = "up"
        self.root.current = item_text
    
    #self.root.ids.screen_manager.current = item_text
        

    def build(self):
        self.playicons = [MDFloatingActionButton(icon="play", pos_hint={"center_x": .5, "center_y": .5},opacity= 0,on_release= lambda x: self.mainpage_to_streampage('streampage_f1')),
                          MDFloatingActionButton(icon="play", pos_hint={"center_x": .5, "center_y": .5},opacity= 0,on_release= lambda x: self.mainpage_to_streampage('streampage_wrc')),
                          MDFloatingActionButton(icon="play", pos_hint={"center_x": .5, "center_y": .5},opacity= 0,on_release= lambda x: self.mainpage_to_streampage('streampage_dakar')),
                          MDFloatingActionButton(icon="play", pos_hint={"center_x": .5, "center_y": .5},opacity= 0,on_release= lambda x: self.mainpage_to_streampage('streampage_wec'))]
        self.item = [Box(),Box(),Box(),Box()]
        self.is_expanded = [False]*4
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)
    
LabelBase.register(name='F1_font', 
                fn_regular='Formula1-Regular.ttf')
LabelBase.register(name='F1_font_bold', 
                fn_regular='Formula1-bold.ttf')
LabelBase.register(name='F1_font_wide', 
                fn_regular='Formula1-wide.ttf')


RacingApp().run()