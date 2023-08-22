# Billions of Wildcards for Stable Diffusion Dynamic Prompts Extension
Checkout the Descriptions at civitai.

##Usage

Unleash the full power:

Activate: Dynamic Prompts->Advanced Options->Unlink seed from prompt

__Usage__ is pretty much the same as for "regular" wildcards.

You need the SD Dynamic Prompt Extension. Put the files directly into the wildcard folder:
```
~\stable-diffusion-webui\extensions\sd-dynamic-prompts\wildcards 
```
They show up as a menu on the left in the Wildcards tab.

The YAML is structured and indented (that's how they work). Just with a little difference. You have to add the category layers in the wildcard.

Example for a female character:
```
__BoChars/female/modern__
`` 
A cool thing you can do, too, is using a wildcard "*" in the wildcards. So you could use the magical chararcter wildcards in the same prompt and get chars from both sets:
```
__BoChars*/female/modern__
__clothings*__ # for clothings from both sets
```
I made those easy to use cards for character creations. There are some wildcards that are not used for it. Have a look what's in there, too. You'll find a full list below. (another nice part of YAMLs)
You are welcome

## Content
### Billions of Characters
https://civitai.com/models/112041
```
BoChars:
    female:
        modern:
        BoConstructions:
    male:
        modern:
        BoConstructions:
    div:
    random:
clothings:
    female-attire:
    male-attire:
    female:
        upper-body:
        lower-body:
        footwear:
        headwear:
    male:
        upper-body:
        lower-body:
        footwear:
        headwear:
    unisex:
        backwear:
        facewear:
        accesoires:
        neckwear:
person:
    female:
    male:
    ages:
    bodyshapes:
    ears:
    noses:
    chin:
    jaw:
    cheek:
    forehead:
    face-shape:
    body-feature:
    expressions:
    ethnics:
    eyecolor:
    haircolor:
    haircolor-unconv:
    facial-features:
    haircuts-female:
    haircuts-male:
    makeup:
    beard:
    poses:
properties:
    colors:
        common:
        fashion:
        special:
    patterns:
        2Dshapes:
        3Dshapes:
        lines:
        clothing:
    fabric:
matter:
    state:
    movement1:
    movement2:
random:
    color:
    dress-properties:
    accesoires:
    haircolor:
scenes:
    dark:
    gates_magical:
    heaven:
    hell:
    light:
    nature:
    sky-space:
    underground:
    underwater:
```

### Billions of Characters - Magic extension
https://civitai.com/models/111567
```
BoCharsMag:
    female:
        classic:
        modern:
        scenery:
        BoConstructions:
    male:
        classic:
        modern:
        scenery:
        BoConstructions:
    div:
    random:
clothings-magical:
    female-attire:
    male-attire:
    female:
        upper-body:
        full-body:
        lower-body:
        footwear:
        headwear:
    male:
        upper-body:
        full-body:
        lower-body:
        footwear:
        headwear:
    unisex:
        accesoires:
        backwear:
        facewear:
        neckwear:
person-magical:
    female:
    male:
    poses:
    wings:
magical:
    magic:
    types:
        air:
        dark:
        divination:
        dream:
        earth:
        elemental:
        fire:
        gravity:
        ice:
        illusion:
        light:
        lightning:
        metal:
        nature:
        shadow:
        tech:
        time:
        transmutation:
        water:
    beings:
    elemental:
    lighting:
    profession:
        crafter:
        caster:
        knowledge:
        nature:
        dark:
        light:
        illusion:
        technomancy:
    profession-magic-use:
        crafter:
        caster:
        knowledge:
        nature:
        dark:
        light:
        illusion:
        technomancy:
    words:
        adjectives:
        substantives:
        verbs:
properties:
    materials-magic:
        ingredients:
phenomena:
    natural:
    abstract:
random:
    accesoires-magical:
    properties-magical:
    profession-magic:
```

### Billions of Characters - SciFi extension
https://civitai.com/models/115270
```
BoCharsScifi:
    female:
        classic:
        scenery:
        BoConstructions:
    male:
        classic:
        scenery:
        BoConstructions:
    random:
clothings-scifi:
    female-attire:
    male-attire:
    female:
        upper-body:
        full-body:
        lower-body:
        footwear:
        headwear:
    male:
        upper-body:
        full-body:
        lower-body:
        footwear:
        headwear:
    unisex:
        accesoires:
        backwear:
        facewear:
        neckwear:
person-scifi:
    female:
    male:
    poses:
    equipment:
    wings:
scifi:
    types:
    beings:
    lighting:
    profession:
        Technology:
        Exploration:
        Medicine:
        Law-and-Order:
        Entertainment:
        Terraforming:
        Commerce:
        Military:
        Communication:
        Archaeology:
    words:
        adjectives:
        substantives:
        verbs:
phenomena:
    natural-scifi:
    abstract-scifi:
properties:
    pattern:
        clothing-scifi:
    fabric-scifi:
scenes-scifi:
    Futuristic-Cityscape:
    Alien-Planet-Exploration:
    Space-Station-Interiors:
    Cyberpunk-Streets:
    Galactic-Space-Battles:
    Post-Apocalyptic-Wasteland:
    AI-Dominance:
    Interstellar-Travel:
    AI-Integration:
random:
    accesoires-scifi:
    dress-properties-scifi:
    profession-scifi:
```

### Billions of Characters - Cyberpunk extension
https://civitai.com/models/115274
```
BoCharsCyberpunk:
    female:
        classic:
        scenery:
        BoConstructions:
    male:
        classic:
        scenery:
        BoConstructions:
    random:
clothings-cyberpunk:
    female-attire:
    male-attire:
    female:
        upper-body:
        full-body:
        lower-body:
        footwear:
        headwear:
    male:
        upper-body:
        full-body:
        lower-body:
        footwear:
        headwear:
    unisex:
        accesoires:
        backwear:
        facewear:
        neckwear:
person-cyberpunk:
    female:
    male:
    poses:
    equipment:
    wings:
cyberpunk:
    types:
    beings:
    lighting:
    profession:
        Cybernetic-Enhancement:
        Information-Brokers:
        Corporate:
        Outlaws:
        Medics:
        Artists:
        Mercenaries:
        Investigators:
        Engineers:
        Designers:
    words:
        adjectives:
        substantives:
        verbs:
properties:
    patterns:
        clothing-cyberpunk:
    fabric-cyberpunk:
phenomena:
    natural:
    abstract:
scenes-cyberpunk:
    Urban Dystopia:
    Cybernetic Augmentation:
    Virtual Reality Matrix:
    Tech Noir Nightclub:
    Corporate Mega-Corporations:
    Underground Resistance:
    Cyberpunk Noir Detective:
    Techno-Militarized Zone:
    Artificial Intelligence Uprising:
    Post-Apocalyptic Cyberworld:
random:
    accesoires-cyberpunk:
    dress-properties-cyberpunk:
    profession-cyberpunk:
```

### Billions of Constructions
https://civitai.com/models/115641
```
BoConstructions:
    building-standard:
    building-cyberpunk:
    building-scifi:
    building-magical:
    room-standard:
    room-cyberpunk:
    room-scifi:
    room-magical:
    random-building:
    random-room:
    random:
    random-standard:
constructions:
    types:
        Residential-Buildings:
        Commercial-Buildings:
        Educational-Buildings:
        Healthcare-Buildings:
        Industrial-Buildings:
        Recreational-Buildings:
        Government-Buildings:
        Religious-Buildings:
        Transportation-Buildings:
        Special Purpose-Buildings:
    types-fictional:
        residential:
        commercial:
        governmental:
        educational:
        recreational:
        industrial:
    types-cyberpunk:
        Corporate-Megatowers:
        Underground-Cyber-Bunkers:
        Arcade-and-Entertainment-Complexes:
        High-Tech-Medical-Facilities:
        Mega-Marketplaces-and-Bazaars:
        Cyberpunk-Nightclubs:
        Cyberspace-Data-Towers:
        Cyberpunk-Residential-Complexes:
        Cyberpunk-Street-Hangouts:
        Cyberpunk-Factories-and-Assembly-Plants:
    types-scifi:
        Spaceship-Bridges-and-Command-Centers:
        Interstellar-Research-and-Exploration:
        Extraterrestrial-Diplomacy-and-Relations:
        Futuristic-Cybernetic-Cities:
        Advanced-Extraterrestrial-Labs:
        AI-Controlled-Planetary-Defense:
        Time-Travelling-Research-Facilities:
        High-Tech-Cyber-Casinos:
        Extraterrestrial-Artifact-Museums:
        Interstellar-Transportation-Hubs:
    types-magical:
        Enchanted-Schools-of-Magic:
        Celestial-Libraries-of-Knowledge:
        Witch-Covens-and-Magical-Circles:
        Fairy-Tale-Castles-and-Palaces:
        Magical-Taverns-and-Inns:
    rooms:
        Service-Spaces:
        Entertainment-Leisure-Spaces:
        Utility-Spaces:
        Common-Spaces:
        Public-Spaces:
        Living-Spaces:
        Utility-Spaces:
        Public-Spaces:
        Work-Spaces:
        Commercial-Spaces:
        Educational-Spaces:
        Healthcare-Spaces:
        Recreational-Spaces:
        Community-Spaces:
        Transit-Spaces:
        Outdoor-Spaces:
    rooms-fictional:
        Magical-Spaces:
        Mystical-Spaces:
        Fantasy-Spaces:
        Sci-Fi-Spaces:
        Adventure-Spaces:
        Steampunk-Spaces:
        Haunted-Spaces:
        Futuristic-Spaces:
    rooms-scifi:
        Living-Spaces:
        Workspaces:
        Recreational:
        Security-and-Surveillance:
        Medbay-and-Bioengineering-Lab:
        Alien-Encounters:
        Astrobiology-and-Xenobiology:
        Interstellar-Travel:
        Exoplanetary-Exploration:
        Space-Colony-and-Habitat:
    rooms-cyberpunk:
        Living-Spaces:
        Workspaces:
        Recreational:
        Security-and-Surveillance:
        Medbay-and-Cybernetics-Lab:
        Cybernetics-and-Augmentation:
        Darknet-and-Underground:
        Cyberpunk-Street-Scene:
        AI-and-Robotics:
        Cyberspace-and-Virtual Worlds:
    rooms-magical:
        Living-Spaces:
        Workspaces:
        Recreational:
        Security-and-Surveillance:
        Healing-and-Potions:
        Transportation-and-Portals:
        Artifacts-and-Relics:
        Guardians-and-Companions:
        Celestial-Observatories:
        Chambers-of-Prophecy:
        Feywild-Gardens:
    interior-design:
        Furniture:
        Appliances:
        Lighting:
        Bedding-Linens:
        Storage-Organization:
        Decor:
        Electronics:
        Kitchenware:
        Bathroom-Essentials:
        Cleaning-Supplies:
    interior-design-fictional:
        Furniture:
        Magical Artifacts:
        Treasures:
        Technology:
        Ancient Relics:
        Mystical Creatures:
        Tools and Gadgets:
    light-sources-indoor:
        natural:
        fire:
        artificial:
        biological:
    light-sources-outdoor:
        natural:
        artificial:
        biological:
        fire type:
    lighting:
        indoor:
        outdoor:
        specialized:
    features:
        tiny:
        small:
        medium:
        big:
        huge:
        large:
        mega:
properties:
    patterns:
        tapestry:
    materials-construction:
        stones:
        basic:
        fictional:
        cyberpunk:
        scifi:
        roofing:
        Insulation:
        Flooring:
styles:
    art-styles:
    punk-styles:
random:
    materials-indoor:
    materials-outdoor:
    light-source-indoor:
    light-source-outdoor:
    lighting-indoor:
    lighting-outdoor:
    interior-design:
    interior-design-fictional:
    rooms:
    rooms-fictional:
    rooms-cyberpunk:
    rooms-scifi:
    rooms-magical:
    buildings:
    buildings-fictional:
    buildings-cyberpunk:
    buildings-scifi:
    buildings-magical:
```

### Billions of Characters - NSFW clothing
https://civitai.com/models/115256
```
clothings-nsfw:
    female-attire:
    male-attire:
    female:
        upper-body:
        full-body:
        lower-body:
        underwear-upper:
        underwear-lower:
        footwear:
        headwear:
    male:
        upper-body:
        full-body:
        lower-body:
        footwear:
        headwear:
    unisex:
        accesoires:
        backwear:
        facewear:
        neckwear:
person-nsfw:
    poses:
NSFW:
    lighting:
    materials:
    words:
        adjectives:
        substantives:
        verbs:
properties:
    patterns:
        animal-print:
random:
    dress-properties-nsfw:
    accesoires-nsfw:
```

### Billions of Styles
https://civitai.com/models/117222
```
BoStyles:
    random-anything:
    random-artstyle:
    random-punk-styles:
    random-atmosphere:
    random-atmosphere-Light:
    random-atmosphere-Dark:
    random-atmosphere-Colorful:
    random-atmosphere-Intense:
    random-atmosphere-Serene:
    random-atmosphere-Cozy:
    random-atmosphere-Mysterious:
    random-atmosphere-Romantic:
    random-atmosphere-Melancholic:
    random-atmosphere-Magical:
    random-atmosphere-Rustic:
    random-atmosphere-Ethereal:
    random-atmosphere-Dramatic:
    random-atmosphere-Nostalgic:
    random-atmosphere-Festive:
    random-atmosphere-Minimalist:
    random-atmosphere-Majestic:
    random-atmosphere-Surreal:
    random-atmosphere-Urban:
    random-rendering:
    random-rendering-Ray-Tracing:
    random-rendering-Ambient-Effects:
    random-rendering-Particles-and-Effects:
    random-rendering-Lighting-Techniques:
    random-rendering-Shading-Techniques:
    random-rendering-Mapping-Techniques:
    random-rendering-Post-Processing-Techniques:
    random-rendering-Optimization-Techniques:
    random-rendering-Artistic-Rendering:
    random-graphic-engines:
    random-image-styles:
    random-image-techniques:
    random-image-techniques-Traditional:
    random-image-techniques-Digital:
    random-image-techniques-Photographic:
    random-image-techniques-Other:
    random-depiction-styles:
    random-depiction-styles-2D-Styles:
    random-depiction-styles-3D-Styles:
    random-depiction-styles-Historical:
    random-depiction-styles-Digital-Modern-Styles:
    random-animation-style:
    random-ambient-effect:
    random-quality-prompts:
    random-resolution:
    random-creative-concept:
    random-camera-settings:
styles:
    art-styles:
    punk-styles:
    atmosphere:
        Light:
        Dark:
        Colorful:
        Intense:
        Serene:
        Cozy:
        Mysterious:
        Romantic:
        Melancholic:
        Magical:
        Rustic:
        Ethereal:
        Dramatic:
        Nostalgic:
        Festive:
        Minimalist:
        Majestic:
        Surreal:
        Urban:
        Mystical:
    rendering-techniques:
        Ray-Tracing:
        Ambient-Effects:
        Particles-and-Effects:
        Lighting-Techniques:
        Shading-Techniques:
        Mapping-Techniques:
        Post-Processing-Techniques:
        Optimization-Techniques:
        Artistic-Rendering:
        Advanced-Rendering:
    graphic-engines:
    image-styles:
    image-techniques:
        Traditional:
        Digital:
        Photographic:
        Other:
    depiction-styles:
        2D-Styles:
        3D-Styles:
        Historical:
        Digital-Modern-Styles:
    animations:
    Ambient-Effects:
    quality:
        details:
        styles:
        sharp:
        blur:
    resolutions:
    Creative-Concepts:
    camera:
        Camera:
        Aperture-Settings:
        Shutter-Speed:
        ISO-Settings:
        White-Balance:
        Exposure-Settings:
        Shooting-Modes:
        Composition-Techniques:
        Focus:
        Metering:
constructors:
shape-tracing:
surface-swap:
```

### Billions of Creatures
https://civitai.com/models/130497
```
BoCreatures:
    random:
creatures:
    size:
    horns:
    Mouth-Jaw:
    traits:
    descriptors:
    Look-Feel:
    nmbrlegs:
    nmbrarms:
    nmbrtails:
    tails:
    Appendages:
    Body-Shapes:
    Skin-Fur-Types:
    Ear-Types:
    wings:
properties:
    colors:
        common:
        animal-print:
    Patterns:
        unusual:
```

### Billions of Vehicles
https://civitai.com/models/131367
```
# Billions of vehicles:
BoVehicles:
    random:
    random-scifi:
    random-notype:
vehicles:
    size:
    types:
        train:
        space:
        Cars:
        Motorcycles:
        Bicycles:
        Heavy-Vehicles:
        Public Transport:
        Special-Purpose:
        Fictional-Concept:
        Airborne-Vehicles:
        Flying-Car-Like-Vehicles:
        Underwater-Vehicles:
        Fictional-Underwater-Vehicles:
        Underground-Vehicles:
    exterior-features:
    windows:
    lights:
    Accessories:
    Customization:
properties:
    materials-vehicles:
    Visual-Appearance:
    paint-vehicle:
    Texture-vehicles:
```

### Billions of Plants/Shrooms
https://civitai.com/models/132782
```
BoPlants:
    random-plant:
    random-shroom:
plants:
    types:
    Growth-Habit:
    Leaf:
    Flower:
    Fruit:
    Stem:
    Foliage-Arrangement:
    Inflorescence:
    Leaf-Venation:
    Sepal-Configuration:
    Seed:
    Leaf-Margin:
    Leaf-Arrangement:
mushrooms:
    types:
    Gill:
    Veil:
    Ring:
    Bruising:
    Annulus:
    Volva:
    Pileus:
    Pores:
    Hymenium:
    Stipe-Base:
    Latex:
    Mycorrhizal-Association:
    Habitat:
    Growth-Form:
    Bioluminescence:
    Poisonous-Properties:
    Medicinal-Properties:
properties:
    colors:
        plants:
        mushrooms:
        Spore-Print:
        Stipe:
        Gill:
    size:
        plants:
        mushrooms:
    shape:
        plants:
        mushrooms:
        leaf:
        Petal:
        stem:
        bud:
    texture:
        stem:
        mushrooms:
        Bark:
        plants:
    pattern:
        mushrooms:
        plants:
    structure:
        root:
```

### Magic Only
https://civitai.com/models/111464
```
magic:
    magic:
    words:
        adjectives:
        substantives:
        verbs:
        colors:
            common:
            fashion:
            special:
        patterns:
            2Dshapes:
            3Dshapes:
            lines:
        materials-magic:
    phenomena:
        natural:
        abstract:
        Phase-Changes:
    matter:
        state:
        movement1:
        movement2:
```

### Dr.Derp cards
https://civitai.com/models/116021
```
dr.derp-hypernetworks:
    front-shot:
        full-body:
        medium-shot:
        cowboy-shot:
        upper-body-shot:
        close-up-shot:
        extreme-close-up-shot:
    side-shot:
        full-body:
        medium-shot:
        cowboy-shot:
        upper-body-shot:
        close-up-shot:
        extreme-close-up-shot:
    profile-shot:
        full-body:
        medium-shot:
        cowboy-shot:
        upper-body-shot:
        close-up-shot:
        extreme-close-up-shot:
    back-side-shot:
        full-body:
        medium-shot:
        cowboy-shot:
        upper-body-shot:
        close-up-shot:
        extreme-close-up-shot:
    back-shot:
        full-body:
        medium-shot:
        cowboy-shot:
        upper-body-shot:
        close-up-shot:
        extreme-close-up-shot:
weight:
    strong:
    moderate:
    medium:
    modest:
    weak:
```

