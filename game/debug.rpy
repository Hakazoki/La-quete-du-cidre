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

screen barre_seduction():
    zorder 999

    fixed:
        xalign 0.5 
        ypos 50
        xsize 400 ysize 80 

        
        add Solid("#330000aa") xsize 400 ysize 80 xalign 0.5

        
        $ bar_val = max(0, min(100, (seduction + 50) / 2))
        bar:
            value bar_val
            range 100
            xsize 380
            ysize 30 
            xalign 0.5
            ypos 25  
            unscrollable "unscrollable"

        
        if seduction > 100:
            $ extension_droite = (seduction - 100) * 4
            add Solid("#ffaa44"):
                xsize extension_droite ysize 30
                ypos 25   
                xpos 400   
                xanchor 0.0

        
        if seduction < -50:
            $ extension_gauche = (abs(seduction) - 50) * 4
            add Solid("#ff4444"):
                xsize extension_gauche ysize 30
                ypos 25
                xpos 0     
                xanchor 1.0

        
        text "Niveau de Sympathie/Obsession : [seduction]%" size 18 xalign 0.5 ypos 5
        
        
        if seduction <= -50:
            text "{b}{color=#ff0000}ERREUR : PURETÉ CRITIQUE{/color}{/b}" size 14 xalign 0.5 ypos 60
        elif seduction >= 150:
            text "{b}{color=#ff00ff}ALERTE : OBSESSION{/color}{/b}" size 14 xalign 0.5 ypos 60