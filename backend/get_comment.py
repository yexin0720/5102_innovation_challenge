import random
def sarcastic_comment(traffic_condition):
    jam = ["Oh, a traffic jam? How delightfully unexpected during rush hour. Here's a thought: have you considered turning your car into a helicopter? No? Too bad. Alternatively, you could always make friends with the folks in the car next to you. It's going to be a long bonding session.",
           "Back to the traffic jam, are we? How nostalgic. Well, in that case, consider it the universe's way of saying you deserve a break. Why not take this opportunity to learn a new language? By the time you move another inch, you could be fluent in conversational honking.",
           "Ah, still stuck? Well, at this point, you might as well start writing a memoir titled 'My Life in Traffic: An Ode to Lost Time.' Who knows? By the time you reach your destination, you might have a bestseller on your hands."]
    empty = ["Empty roads, you say? What a plot twist! This is your moment to pretend you're the main character in a post-apocalyptic movie, where the streets are yours and yours alone. Just remember, the only things chasing you are deadlines and perhaps a squirrel or two. Enjoy the cinematic freedom—just don't get too used to it. Reality tends to reboot with traffic at the most inconvenient times.",
             "Empty again? Wow, it seems like everyone else got the memo to teleport to work today. You could practically do a leisurely marathon on the highway now, couldn't you? Just be wary of the occasional tumbleweed or bewildered pedestrian crossing the road—they might be just as surprised as you are to find such open space in the wild urban jungle.",
             "Oh, the emptiness persists? It seems you've stumbled into a parallel universe where traffic doesn't exist. Congratulations! Now's the perfect time to practice those parade waves or perhaps that victory lap you've always dreamed of. Just beware of accidentally shifting back into the regular, traffic-laden universe. The transition can be quite jarring."]
    high = ["High traffic, you say? Well, it's the perfect opportunity to become an expert in the art of stationary vehicle meditation. Transform your car into a zen garden on wheels (honking horns and all). Embrace the stillness, breathe in the exhaust, and exhale patience. You're not stuck in traffic; you're in a mobile retreat. Enlightenment, here you come!",
            "Ah, the high traffic saga continues. It's like being in a grand parade, except everyone's competing for the slowest float. Perhaps now's the time to brainstorm solutions to world peace or solve complex math problems in your head. With the pace you're moving, you might just crack the code to universal harmony—or at least figure out the most efficient way to organize your grocery list."]
    low = ["Low traffic now? How the tables have turned. Seize this unexpected freedom like a squirrel discovering an unguarded bird feeder. You could actually make it to your destination early and bask in the luxury of spare time. Just remember, low traffic is like a mythical creature: often spoken of, but rarely seen. Enjoy the sighting while it lasts!",
           "Low traffic again? It's like finding a unicorn two times in a row! This is your chance to feel like a VIP with the roads cleared just for you. Maybe do a victory lap, or simply enjoy the breeze without the symphony of honks. Just don't get too used to it; you wouldn't want to be shocked back into reality when the traffic decides to return from its coffee break."]
    medium = ["Medium traffic, huh? That's the traffic equivalent of 'meh'. It's not bad enough to complain about, but not good enough to celebrate, either. It's like being in limbo, where you're constantly debating whether to be frustrated at the slow pace or grateful it's moving at all. Perhaps this is the universe's way of teaching patience, or maybe it's just Tuesday.",
              "Ah, medium traffic again. This is the traffic that can't quite decide what it wants to be when it grows up. It's the adolescent phase of road congestion, full of potential yet lacking clear direction. You're moving, but not too fast, giving you ample time to ponder life's mysteries—like why we don't see more bumper stickers with philosophical quotes. A perfect moment for moderate reflection amidst moderate movement."]
    if traffic_condition == "Traffic Jam":
        return random.choice(jam)
    elif traffic_condition == "Empty":
        return random.choice(empty)
    elif traffic_condition == "High":
        return random.choice(high)
    elif traffic_condition == "Low":
        return random.choice(low)
    elif traffic_condition == "Medium":
        return random.choice(medium)
    else:
        return "I'm sorry, I don't understand. Think twice before you speak, human."
    
if __name__ == "__main__":
    traffic_condition = "High"
    print(sarcastic_comment(traffic_condition))