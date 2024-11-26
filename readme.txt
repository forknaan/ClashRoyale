Description:
    CMU Royale
    A PvE/PvP battle game centered around strategy. Each player will have a deck 
    and be allowed to play cards to defeat the opponent's towers and get crowned 
    victory.

Competitive Analysis:
    This game is inspired and mainly based off a similar successful game called 
    Clash Royale which is a mobile game. I plan to inherit the original games 
    mechanics, however there will be some smaller design changes to allow for 
    more efficient code in CMU-graphics.

Structural Plan: 
    I have broken my project into multiple files, the main file, the home file, 
    the arena file. For the cards I am using a classes to represent them with their
    attributes and also to allow multiple instances of that class on the map at 
    one time.

Algorithmic Plan:
    Algorithms to deal with:
    1. There is the movement of all cards, moving to the nearest enemy on the map or
    tower, while also following a relatively accurate path to the king tower. This
    involes manipulation of straight lines and a few checking function.
    (Implemented as of MVP)

    2. There is the collision of characters, how they are to move when colliding
    with other objects. 
        - Doing various checks to ensure no collisions, and if so then move 
        character relative to their location on the map 
    (Un-implemented as of MVP)

    3. The various different attack methods of each card, from splash damage, to 
    long range firing of projectiles, to instantaneous damage dealing.
    (Implemented as of MVP)

    4. The AI the player will be playing at and how to manage its difficulty
        - I plan on countering this issue by trying to write down my reasoning
        of how to play, as if I am the AI, to create a more advanced AI to play
        against
    (partially implemented as of MVP)

    (Bonus)
    5. Implementing Local Multiplayer via Socket.
        - I plan on doing this by first adding a loading screen for waiting for
        connections and jsut mapping the connected user as enemy and just 
        translating their moves to the user.
    (Un-implemented as of MVP)

Timeline Plan:
    Deadlines:
        MVP is reached by 26th November
        Project is fully playable by 3rd December

    Features:
        Add Projectile Class for ranged cards as well fix cooldown issues by
        28th November
        Add a game Timer as well as better AI levels by 28th November
        Add socket implementation of Multiplayer by 30th November
        Add Nice UI and fully working Sprite Graphics by 2nd December


Version Control Plan:
I am employing the use of GitHub for backup.

Module List:
I only plan on using CMU-graphics until my MVP, possibly employ the use of 
Socket after MVP.


TP 2 Update:
The whole design Docs have been updated to match the current project what is
being done, with more in-depth detail of all important features and Timelines.
Overall, there is no massive change to the original game itself.
(Primarily Added more stuff to Timeline and Algorithmic Plan)