screen debug_class_menu():
    modal True
    zorder 200 
    
    style_prefix "debug"

    frame:
        xalign 0.5 yalign 0.5
        background Solid("#1a1a1ae6") 
        padding (30, 30)
        
        vbox:
            spacing 15
            label "{b}DEBUG : CHANGEMENT DE CLASSE{/b}" xalign 0.5
            
            null height 10

            
            textbutton "Devenir BARBARE" action [SetVariable("pc", Barbare()), Hide("debug_class_menu")]
            textbutton "Devenir VOLEUR" action [SetVariable("pc", Voleur()), Hide("debug_class_menu")]
            textbutton "Devenir MAGE" action [SetVariable("pc", Mage()), Hide("debug_class_menu")]
            textbutton "Devenir ÉLU DE MORADIN" action [SetVariable("pc", EluDeMoradin()), Hide("debug_class_menu")]
            textbutton "Devenir TAVERNIER" action [SetVariable("pc", Tavernier()), Hide("debug_class_menu")]
            
            null height 20
            
            textbutton "FERMER" action Hide("debug_class_menu") xalign 0.5 text_color "#ff4444"

style debug_button:
    xsize 400                      
    background Solid("#333")       
    padding (10, 10)
    hover_background Solid("#555") 

style debug_button_text:
    xalign 0.5                     
    yalign 0.5                     
    size 22
    idle_color "#ffffff"
    hover_color "#00ff00"