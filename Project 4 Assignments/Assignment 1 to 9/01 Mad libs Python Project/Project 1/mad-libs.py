def mad_libs():
    print("Mad Libs Game Start!")
    
    noun = input("Ek noun do (jaise: dog): ")
    verb = input("Ek verb do (jaise: run): ")
    adjective = input("Ek adjective do (jaise: funny): ")
    place = input("Ek jagah ka naam do (jaise: park): ")

    story = f"Ek {adjective} {noun} {place} mein tha aur wo {verb} kar raha tha."
    
    print("\n--- Tumhari Story ---")
    print(story)

mad_libs()
