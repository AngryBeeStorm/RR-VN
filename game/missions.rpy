# missions.rpy



image folder_icon = "images/folder-icon.png"


default main_missions = [
    {"name": "Mission Alpha", "description": "\nJob Description: Artifact retrieval and delivery.\nRisk Level: Low (too boring for ya, newbie?)\nPick-up Location: Ursa Major Flower Saloon\nDelivery Location: Gilded Globe Ventures\nTime Frame: Package should be delivered by 10 AM today.", "mission_label": "felix_runin"},
    {"name": "Mission Beta", "description": "Explore the Alpha sector. \nTry to find the least annoying human on earth", "mission_label": "tian_meeting"},
    {"name": "Mission Gamma", "description": "Secure the base perimeter.\nTry to find the least annoying human on earth", "mission_label": "felix_runin"}
]

default first_mission = [
    {"name": "Mission \nFetch", "description": "Transport artifact.", "mission_label": "felix_runin"},
]


# Function to display missions dynamically based on content of all_missions
screen missions_screen(): #mission_list):
    default selected_mission = {}
    zorder 100  # Ensures this screen appears above others
    add "gui/futuristic_overlay.png" at right

    hbox:
        xalign 0.5
        yalign 0.4
        spacing 50
        hbox:
            style_prefix "mission"
            for i, mission in enumerate(main_missions):
                textbutton mission["name"] style "mission_textbutton" action [SetVariable("selected_mission", mission), Show("mission_detail_screen")]#Jump(details_label)]
            

screen mission_detail_screen():
    on "show" action Function(renpy.log, f"Showing details for: {selected_mission}")
    $ mission_action = Jump(selected_mission['mission_label']) 
    zorder 102
    modal True  # Makes the screen block interaction below it
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "[selected_mission['name']]"
            text "[selected_mission['description']]"
            textbutton "Accept" action [Hide("mission_detail_screen"), mission_action]
            textbutton "Back" action Hide("mission_detail_screen")




style mission_textbutton:
    yalign 0.3
    idle_background Solid("#111111")
    hover_background Solid("#AAAAAA")
    ypadding 10
    xmargin 20


style my_custom_button:
    xalign 0.5
    yalign 0.5
    background Solid("#333333")