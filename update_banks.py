# -*- coding: utf-8 -*-
import json
import re

qbank = [
  # SCIENCE (22 questions)
  {"q": "What planet is known as the Red Planet?", "o": ["Mars", "Venus", "Jupiter", "Saturn"], "a": 0, "c": "science"},
  {"q": "What gas do plants absorb during photosynthesis?", "o": ["Carbon Dioxide (CO₂)", "Oxygen (O₂)", "Nitrogen (N₂)", "Hydrogen (H₂)"], "a": 0, "c": "science"},
  {"q": "How many bones are in an adult human body?", "o": ["206", "210", "198", "215"], "a": 0, "c": "science"},
  {"q": "What is the largest organ in the human body?", "o": ["Skin", "Liver", "Heart", "Brain"], "a": 0, "c": "science"},
  {"q": "What is the chemical symbol for water?", "o": ["H₂O", "CO₂", "NaCl", "O₂"], "a": 0, "c": "science"},
  {"q": "Which planet has the most confirmed moons?", "o": ["Saturn", "Jupiter", "Uranus", "Neptune"], "a": 0, "c": "science"},
  {"q": "What type of vertebrate animal is a frog?", "o": ["Amphibian", "Reptile", "Mammal", "Fish"], "a": 0, "c": "science"},
  {"q": "Which vitamin is synthesised by our skin in sunlight?", "o": ["Vitamin D", "Vitamin C", "Vitamin A", "Vitamin B"], "a": 0, "c": "science"},
  {"q": "What is the hardest natural mineral on Earth?", "o": ["Diamond", "Gold", "Iron", "Quartz"], "a": 0, "c": "science"},
  {"q": "How many legs does an adult spider possess?", "o": ["8", "6", "10", "12"], "a": 0, "c": "science"},
  {"q": "Which organelle is called the powerhouse of the cell?", "o": ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"], "a": 0, "c": "science"},
  {"q": "Which gas constitutes about 78% of Earth's atmosphere?", "o": ["Nitrogen", "Oxygen", "Argon", "Carbon Dioxide"], "a": 0, "c": "science"},
  {"q": "What green pigment enables plants to perform photosynthesis?", "o": ["Chlorophyll", "Carotene", "Xanthophyll", "Melanin"], "a": 0, "c": "science"},
  {"q": "Sound waves cannot travel through which of the following?", "o": ["Vacuum", "Water", "Steel", "Air"], "a": 0, "c": "science"},
  {"q": "What fundamental force keeps the Earth orbiting the Sun?", "o": ["Gravitational force", "Magnetic force", "Nuclear force", "Frictional force"], "a": 0, "c": "science"},
  {"q": "At what temperature Celsius does pure water freeze?", "o": ["0°C", "32°C", "-4°C", "10°C"], "a": 0, "c": "science"},
  {"q": "Which part of the human eye detects light and colour?", "o": ["Retina", "Cornea", "Iris", "Pupil"], "a": 0, "c": "science"},
  {"q": "What is the nearest star to planet Earth?", "o": ["The Sun", "Proxima Centauri", "Sirius", "Alpha Centauri"], "a": 0, "c": "science"},
  {"q": "Which metal remains in a liquid state at room temperature?", "o": ["Mercury", "Bromine", "Gallium", "Lead"], "a": 0, "c": "science"},
  {"q": "How many chambers are there in the human heart?", "o": ["4", "2", "3", "6"], "a": 0, "c": "science"},
  {"q": "What is the chemical formula for common table salt?", "o": ["NaCl", "KCl", "NaHCO₃", "CaCO₃"], "a": 0, "c": "science"},
  {"q": "Which blood cells are responsible for fighting infections?", "o": ["White Blood Cells", "Red Blood Cells", "Platelets", "Plasma"], "a": 0, "c": "science"},

  # MATH (22 questions)
  {"q": "What is 15 × 15?", "o": ["225", "215", "250", "200"], "a": 0, "c": "math"},
  {"q": "What is the square root of 144?", "o": ["12", "14", "11", "13"], "a": 0, "c": "math"},
  {"q": "How many sides does a regular hexagon have?", "o": ["6", "5", "7", "8"], "a": 0, "c": "math"},
  {"q": "What is the approximate value of π (Pi) to 2 decimals?", "o": ["3.14", "3.16", "3.12", "3.18"], "a": 0, "c": "math"},
  {"q": "The sum of interior angles in a triangle is always?", "o": ["180°", "360°", "90°", "270°"], "a": 0, "c": "math"},
  {"q": "What is 25% of 200?", "o": ["50", "40", "60", "45"], "a": 0, "c": "math"},
  {"q": "What is the next prime number after 7?", "o": ["11", "9", "13", "8"], "a": 0, "c": "math"},
  {"q": "How many zeros are there in one million (1,000,000)?", "o": ["6", "5", "7", "8"], "a": 0, "c": "math"},
  {"q": "What is 7 cubed (7³)?", "o": ["343", "349", "337", "351"], "a": 0, "c": "math"},
  {"q": "What is 1000 ÷ 8?", "o": ["125", "120", "130", "115"], "a": 0, "c": "math"},
  {"q": "What is the square of 19 (19 × 19)?", "o": ["361", "341", "381", "391"], "a": 0, "c": "math"},
  {"q": "How many faces does a cube or cuboid have?", "o": ["6", "8", "12", "4"], "a": 0, "c": "math"},
  {"q": "An item costs ₹500. After a 20% discount, what is its price?", "o": ["₹400", "₹420", "₹380", "₹450"], "a": 0, "c": "math"},
  {"q": "What is the perimeter of a square whose side is 9 cm?", "o": ["36 cm", "81 cm", "27 cm", "45 cm"], "a": 0, "c": "math"},
  {"q": "What is 2 raised to the power of 8 (2⁸)?", "o": ["256", "128", "512", "64"], "a": 0, "c": "math"},
  {"q": "How many total seconds are there in 2 hours?", "o": ["7,200", "3,600", "1,200", "6,000"], "a": 0, "c": "math"},
  {"q": "What is the only even prime number in mathematics?", "o": ["2", "4", "0", "6"], "a": 0, "c": "math"},
  {"q": "An angle that measures exactly 90 degrees is called a?", "o": ["Right angle", "Acute angle", "Obtuse angle", "Reflex angle"], "a": 0, "c": "math"},
  {"q": "What is the average (mean) of 10, 20, 30, and 40?", "o": ["25", "20", "30", "24"], "a": 0, "c": "math"},
  {"q": "If 3x = 45, what is the value of x?", "o": ["15", "12", "18", "9"], "a": 0, "c": "math"},
  {"q": "How many millimeters are there in 1 meter?", "o": ["1,000", "100", "10,000", "10"], "a": 0, "c": "math"},
  {"q": "What is the Roman numeral for 50?", "o": ["L", "C", "D", "X"], "a": 0, "c": "math"},

  # GENERAL KNOWLEDGE (22 questions)
  {"q": "Which is the largest continent on Earth by area?", "o": ["Asia", "Africa", "Europe", "Antarctica"], "a": 0, "c": "gk"},
  {"q": "What is the capital city of Japan?", "o": ["Tokyo", "Osaka", "Kyoto", "Seoul"], "a": 0, "c": "gk"},
  {"q": "How many distinct colours are traditionally in a rainbow?", "o": ["7", "6", "8", "5"], "a": 0, "c": "gk"},
  {"q": "Which ocean is the largest and deepest on Earth?", "o": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "a": 0, "c": "gk"},
  {"q": "Who is credited with inventing the first practical telephone?", "o": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Albert Einstein"], "a": 0, "c": "gk"},
  {"q": "What is the highest mountain peak in the world above sea level?", "o": ["Mount Everest", "K2", "Kangchenjunga", "Makalu"], "a": 0, "c": "gk"},
  {"q": "How many continents are there on Earth?", "o": ["7", "6", "5", "8"], "a": 0, "c": "gk"},
  {"q": "What is the official currency of Japan?", "o": ["Yen", "Won", "Yuan", "Ringgit"], "a": 0, "c": "gk"},
  {"q": "In which European country is the Eiffel Tower situated?", "o": ["France", "Italy", "Germany", "Spain"], "a": 0, "c": "gk"},
  {"q": "What is the smallest independent country in the world by area?", "o": ["Vatican City", "Monaco", "Nauru", "Malta"], "a": 0, "c": "gk"},
  {"q": "Which continent has no permanent human population or native countries?", "o": ["Antarctica", "Australia", "Europe", "South America"], "a": 0, "c": "gk"},
  {"q": "Which river is traditionally considered the longest in the world?", "o": ["Nile", "Amazon", "Yangtze", "Mississippi"], "a": 0, "c": "gk"},
  {"q": "Which is the largest hot desert in the world?", "o": ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Thar Desert"], "a": 0, "c": "gk"},
  {"q": "What is the capital city of Australia?", "o": ["Canberra", "Sydney", "Melbourne", "Brisbane"], "a": 0, "c": "gk"},
  {"q": "What is the official currency of the United Kingdom?", "o": ["Pound Sterling", "Euro", "Dollar", "Franc"], "a": 0, "c": "gk"},
  {"q": "In which historic city is the ancient Colosseum located?", "o": ["Rome", "Athens", "Paris", "Cairo"], "a": 0, "c": "gk"},
  {"q": "What is the deepest oceanic trench on planet Earth?", "o": ["Mariana Trench", "Puerto Rico Trench", "Java Trench", "Tonga Trench"], "a": 0, "c": "gk"},
  {"q": "Which country presented the Statue of Liberty as a gift to the USA?", "o": ["France", "United Kingdom", "Spain", "Germany"], "a": 0, "c": "gk"},
  {"q": "How many official time zones span across Russia?", "o": ["11", "9", "7", "5"], "a": 0, "c": "gk"},
  {"q": "What is the capital city of Canada?", "o": ["Ottawa", "Toronto", "Vancouver", "Montreal"], "a": 0, "c": "gk"},
  {"q": "Which is the world's largest island that is not a continent?", "o": ["Greenland", "Madagascar", "New Guinea", "Borneo"], "a": 0, "c": "gk"},
  {"q": "What is the primary language spoken in Brazil?", "o": ["Portuguese", "Spanish", "English", "French"], "a": 0, "c": "gk"},

  # SPORTS (22 questions)
  {"q": "How many players are on the field for one team in cricket?", "o": ["11", "10", "12", "9"], "a": 0, "c": "sports"},
  {"q": "Which sport uses a racquet and a shuttlecock?", "o": ["Badminton", "Tennis", "Squash", "Table Tennis"], "a": 0, "c": "sports"},
  {"q": "How many interlocking rings are on the official Olympic flag?", "o": ["5", "4", "6", "7"], "a": 0, "c": "sports"},
  {"q": "Which national team won the 2022 FIFA Men's World Cup?", "o": ["Argentina", "France", "Brazil", "Germany"], "a": 0, "c": "sports"},
  {"q": "How many points is a standard basketball free throw worth?", "o": ["1", "2", "3", "4"], "a": 0, "c": "sports"},
  {"q": "In lawn tennis, what term represents a score of zero?", "o": ["Love", "Nil", "Zero", "Duck"], "a": 0, "c": "sports"},
  {"q": "Which grand slam tennis championship is played on grass courts?", "o": ["Wimbledon", "US Open", "French Open", "Australian Open"], "a": 0, "c": "sports"},
  {"q": "What is the official marathon race distance in kilometres?", "o": ["42.195 km", "40 km", "45 km", "38 km"], "a": 0, "c": "sports"},
  {"q": "How many holes are played in a standard full round of golf?", "o": ["18", "9", "12", "24"], "a": 0, "c": "sports"},
  {"q": "What card is displayed by a football referee to eject a player?", "o": ["Red Card", "Yellow Card", "Blue Card", "Black Card"], "a": 0, "c": "sports"},
  {"q": "How many players are on the court per team in indoor volleyball?", "o": ["6", "5", "7", "8"], "a": 0, "c": "sports"},
  {"q": "In which two years did the Indian men's cricket team win the ODI World Cup?", "o": ["1983 & 2011", "1983 & 2007", "1999 & 2011", "2007 & 2023"], "a": 0, "c": "sports"},
  {"q": "What is the term for rolling three strikes in a row in bowling?", "o": ["Turkey", "Eagle", "Hat-trick", "Triple"], "a": 0, "c": "sports"},
  {"q": "In which ancient country did the Olympic Games originate?", "o": ["Greece", "Italy", "Egypt", "China"], "a": 0, "c": "sports"},
  {"q": "Which board game uses the terms 'Checkmate' and 'Stalemate'?", "o": ["Chess", "Carrom", "Checkers", "Scrabble"], "a": 0, "c": "sports"},
  {"q": "How many wooden bails are placed across the three cricket stumps?", "o": ["2", "3", "1", "4"], "a": 0, "c": "sports"},
  {"q": "Which legendary sprint champion holds the 100m world record of 9.58s?", "o": ["Usain Bolt", "Carl Lewis", "Tyson Gay", "Yohan Blake"], "a": 0, "c": "sports"},
  {"q": "How many players are on the field defensively in baseball?", "o": ["9", "8", "10", "11"], "a": 0, "c": "sports"},
  {"q": "What color belt represents the highest beginner master level in Karate?", "o": ["Black belt", "White belt", "Brown belt", "Red belt"], "a": 0, "c": "sports"},
  {"q": "How many minutes long is each half in standard soccer?", "o": ["45 minutes", "40 minutes", "50 minutes", "30 minutes"], "a": 0, "c": "sports"},
  {"q": "Which Indian city hosted the ICC Men's Cricket World Cup 2023 final?", "o": ["Ahmedabad", "Mumbai", "Kolkata", "Delhi"], "a": 0, "c": "sports"},
  {"q": "In carrom, how many points is the red Queen coin worth with a cover?", "o": ["3 points", "5 points", "2 points", "1 point"], "a": 0, "c": "sports"},

  # INDIA & CURRENT AFFAIRS (25 questions)
  {"q": "Who is revered as the Father of the Nation in India?", "o": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhash Chandra Bose", "Sardar Patel"], "a": 0, "c": "india"},
  {"q": "Children's Day in India is celebrated on whose birth anniversary?", "o": ["Jawaharlal Nehru", "Mahatma Gandhi", "Dr. APJ Abdul Kalam", "Dr. Radhakrishnan"], "a": 0, "c": "india"},
  {"q": "What is the national animal of India?", "o": ["Royal Bengal Tiger", "Asiatic Lion", "Indian Elephant", "Indian Leopard"], "a": 0, "c": "india"},
  {"q": "Which Indian city is globally nicknamed the 'Silicon Valley of India'?", "o": ["Bengaluru", "Hyderabad", "Pune", "Chennai"], "a": 0, "c": "india"},
  {"q": "Who was the first woman of Indian origin to fly into space?", "o": ["Kalpana Chawla", "Sunita Williams", "Tessy Thomas", "Ritu Karidhal"], "a": 0, "c": "india"},
  {"q": "What is the official currency of the Republic of India?", "o": ["Indian Rupee (₹)", "US Dollar ($)", "Taka", "Ringgit"], "a": 0, "c": "india"},
  {"q": "Which is the longest river flowing through India?", "o": ["Ganga", "Godavari", "Yamuna", "Narmada"], "a": 0, "c": "india"},
  {"q": "India's Chandrayaan-3 achieved a historic landing near which lunar region?", "o": ["South Pole of the Moon", "North Pole", "Equator", "Far Side"], "a": 0, "c": "india"},
  {"q": "Who is the President of India?", "o": ["Droupadi Murmu", "Ram Nath Kovind", "Pranab Mukherjee", "Venkaiah Naidu"], "a": 0, "c": "india"},
  {"q": "What does the abbreviation ISRO stand for?", "o": ["Indian Space Research Organisation", "Indian Science Research Org", "Indian Satellite Research Org", "Indo Space Research Office"], "a": 0, "c": "india"},
  {"q": "Which Indian state is the largest in geographic land area?", "o": ["Rajasthan", "Madhya Pradesh", "Maharashtra", "Uttar Pradesh"], "a": 0, "c": "india"},
  {"q": "The world's tallest statue, the Statue of Unity, is located in?", "o": ["Gujarat", "Maharashtra", "Rajasthan", "Madhya Pradesh"], "a": 0, "c": "india"},
  {"q": "Which track & field event did Neeraj Chopra win Olympic Gold in?", "o": ["Javelin Throw", "Shot Put", "Discus Throw", "Long Jump"], "a": 0, "c": "india"},
  {"q": "India's first high-speed bullet train corridor connects Mumbai with?", "o": ["Ahmedabad", "Delhi", "Pune", "Bengaluru"], "a": 0, "c": "india"},
  {"q": "Which major Indian festival is celebrated as the 'Festival of Lights'?", "o": ["Diwali", "Holi", "Eid", "Navratri"], "a": 0, "c": "india"},
  {"q": "How many States currently comprise the Republic of India?", "o": ["28", "29", "30", "27"], "a": 0, "c": "india"},
  {"q": "Who composed the Indian National Anthem 'Jana Gana Mana'?", "o": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Kavi Pradeep"], "a": 0, "c": "india"},
  {"q": "Which historical city in Rajasthan is famously called the 'Pink City'?", "o": ["Jaipur", "Jodhpur", "Udaipur", "Bikaner"], "a": 0, "c": "india"},
  {"q": "What does the instant payment mechanism UPI stand for?", "o": ["Unified Payments Interface", "Universal Payment India", "Unified Pay Integration", "United Payments Interface"], "a": 0, "c": "india"},
  {"q": "Which captain guided India to win the ICC 2011 ODI World Cup?", "o": ["MS Dhoni", "Sachin Tendulkar", "Virat Kohli", "Sourav Ganguly"], "a": 0, "c": "india"},
  {"q": "Who served as the very first Prime Minister of independent India?", "o": ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Lal Bahadur Shastri", "Dr. B.R. Ambedkar"], "a": 0, "c": "india"},
  {"q": "In which Indian state are the famous Ajanta & Ellora caves located?", "o": ["Maharashtra", "Madhya Pradesh", "Karnataka", "Odisha"], "a": 0, "c": "india"},
  {"q": "What is the national aquatic flower of India?", "o": ["Lotus", "Rose", "Jasmine", "Marigold"], "a": 0, "c": "india"},
  {"q": "In which city is the sacred Golden Temple (Harmandir Sahib) located?", "o": ["Amritsar", "Chandigarh", "Ludhiana", "Jalandhar"], "a": 0, "c": "india"},
  {"q": "Which Indian scientist won the Nobel Prize in Physics for the light scattering effect?", "o": ["Sir C.V. Raman", "Dr. Homi Bhabha", "Jagadish Chandra Bose", "Satyendra Nath Bose"], "a": 0, "c": "india"},

  # TRENDING & TECH (22 questions)
  {"q": "What does the abbreviation AI stand for?", "o": ["Artificial Intelligence", "Auto Intelligence", "Advanced Internet", "Applied Info"], "a": 0, "c": "trend"},
  {"q": "Which popular social platform introduced Reels for short viral videos?", "o": ["Instagram", "WhatsApp", "LinkedIn", "Telegram"], "a": 0, "c": "trend"},
  {"q": "The conversational AI service ChatGPT was developed by?", "o": ["OpenAI", "Google", "Meta", "Microsoft"], "a": 0, "c": "trend"},
  {"q": "What is the most subscribed individual YouTube channel in India?", "o": ["T-Series", "CarryMinati", "MrBeast", "PewDiePie"], "a": 0, "c": "trend"},
  {"q": "What does the term 'viral' mean when referring to digital content?", "o": ["Spreading rapidly online across networks", "Infected with malware", "An online video game", "An automated email"], "a": 0, "c": "trend"},
  {"q": "Which mobile game is a famous survival battle royale title?", "o": ["BGMI / PUBG", "Subway Surfers", "Candy Crush", "Chess.com"], "a": 0, "c": "trend"},
  {"q": "What is the commonly cited full form of Wi-Fi?", "o": ["Wireless Fidelity", "Wide Frequency", "Wired Filter", "Web File"], "a": 0, "c": "trend"},
  {"q": "Which social platform was rebranded from Twitter to the letter 'X'?", "o": ["Twitter", "Facebook", "Instagram", "Snapchat"], "a": 0, "c": "trend"},
  {"q": "What is a humorous image or video rapidly shared across the internet called?", "o": ["Meme", "Spam", "Podcast", "GIF"], "a": 0, "c": "trend"},
  {"q": "Which star Indian batsman is widely referred to by fans as 'King Kohli'?", "o": ["Virat Kohli", "Rohit Sharma", "Hardik Pandya", "KL Rahul"], "a": 0, "c": "trend"},
  {"q": "Which multimodal AI model family is developed by Google?", "o": ["Gemini", "Claude", "Copilot", "Llama"], "a": 0, "c": "trend"},
  {"q": "Who is the Indian-born CEO of Google and Alphabet?", "o": ["Sundar Pichai", "Satya Nadella", "Shantanu Narayen", "Arvind Krishna"], "a": 0, "c": "trend"},
  {"q": "Which electric automotive company is led by Elon Musk?", "o": ["Tesla", "Rivian", "Lucid", "Polestar"], "a": 0, "c": "trend"},
  {"q": "What does URL stand for in web browsing addresses?", "o": ["Uniform Resource Locator", "Universal Radio Link", "United Reference Line", "Universal Resource Level"], "a": 0, "c": "trend"},
  {"q": "Which open-world sandbox game allows players to build with 3D blocks?", "o": ["Minecraft", "Roblox", "Fortnite", "Terraria"], "a": 0, "c": "trend"},
  {"q": "What does OTT stand for regarding digital streaming services like Netflix & Hotstar?", "o": ["Over-The-Top", "On-The-Tape", "Online-Tele-Telecom", "Open-To-Town"], "a": 0, "c": "trend"},
  {"q": "In secure web addresses (HTTPS), what does the letter 'S' represent?", "o": ["Secure", "Standard", "System", "Server"], "a": 0, "c": "trend"},
  {"q": "Which ISRO solar observatory was positioned at the Sun-Earth L1 point?", "o": ["Aditya-L1", "Surya-1", "Helios-X", "Solaris-A"], "a": 0, "c": "trend"},
  {"q": "What does PDF stand for in electronic document formats?", "o": ["Portable Document Format", "Printed Data File", "Personal Document Folder", "Packet Data File"], "a": 0, "c": "trend"},
  {"q": "Which battle royale video game is famous for the phrase 'Victory Royale'?", "o": ["Fortnite", "Apex Legends", "Call of Duty", "Free Fire"], "a": 0, "c": "trend"},
  {"q": "Which Indian electric two-wheeler company makes the S1 electric scooter?", "o": ["Ola Electric", "Ather", "TVS", "Bajaj"], "a": 0, "c": "trend"},
  {"q": "What does USB stand for in hardware connection cables?", "o": ["Universal Serial Bus", "United System Board", "Universal Socket Bridge", "Uniform Serial Base"], "a": 0, "c": "trend"},

  # FUN & ENTERTAINMENT (22 questions)
  {"q": "Which Disney fairy tale princess loses a glass slipper at midnight?", "o": ["Cinderella", "Snow White", "Ariel", "Belle"], "a": 0, "c": "fun"},
  {"q": "What is the essential primary green fruit in authentic guacamole?", "o": ["Avocado", "Tomato", "Green Apple", "Kiwi"], "a": 0, "c": "fun"},
  {"q": "How many strings are found on a standard classical guitar?", "o": ["6", "4", "7", "5"], "a": 0, "c": "fun"},
  {"q": "Which majestic big cat is popularly called the 'King of the Jungle'?", "o": ["Lion", "Tiger", "Jaguar", "Leopard"], "a": 0, "c": "fun"},
  {"q": "What geometric shape is a standard highway Stop sign?", "o": ["Octagon (8 sides)", "Hexagon (6 sides)", "Circle", "Pentagon"], "a": 0, "c": "fun"},
  {"q": "In which beloved animated musical do royal sisters Elsa and Anna appear?", "o": ["Frozen", "Tangled", "Moana", "Brave"], "a": 0, "c": "fun"},
  {"q": "What is an infant baby kangaroo officially called?", "o": ["Joey", "Cub", "Pup", "Kit"], "a": 0, "c": "fun"},
  {"q": "How many calendar days occur in a leap year?", "o": ["366 days", "365 days", "364 days", "367 days"], "a": 0, "c": "fun"},
  {"q": "What staple cereal grain is consumed by over half the global human population?", "o": ["Rice", "Wheat", "Maize", "Barley"], "a": 0, "c": "fun"},
  {"q": "What bright color is standard for North American and Indian school buses?", "o": ["Yellow", "Red", "Blue", "Orange"], "a": 0, "c": "fun"},
  {"q": "Who lives in a yellow pineapple under the sea in Bikini Bottom?", "o": ["SpongeBob SquarePants", "Patrick Star", "Squidward", "Sandy Cheeks"], "a": 0, "c": "fun"},
  {"q": "How many books make up J.K. Rowling's original Harry Potter novel series?", "o": ["7", "6", "8", "5"], "a": 0, "c": "fun"},
  {"q": "What is the fastest animal on land over short sprint distances?", "o": ["Cheetah", "Lion", "Pronghorn", "Gazelle"], "a": 0, "c": "fun"},
  {"q": "In Disney Pixar's Toy Story, what kind of toy doll is Sheriff Woody?", "o": ["Cowboy", "Astronaut", "Race Driver", "Soldier"], "a": 0, "c": "fun"},
  {"q": "From which dried fresh fruit are sweet raisins made?", "o": ["Grapes", "Plums", "Figs", "Apricots"], "a": 0, "c": "fun"},
  {"q": "What distinct skin colour characterizes the cartoon characters Smurfs?", "o": ["Blue", "Green", "Purple", "Yellow"], "a": 0, "c": "fun"},
  {"q": "What is the name of Mickey Mouse's loyal pet dog?", "o": ["Pluto", "Goofy", "Bolt", "Snoopy"], "a": 0, "c": "fun"},
  {"q": "How many flexible arms (tentacles) does an octopus have?", "o": ["8", "6", "10", "12"], "a": 0, "c": "fun"},
  {"q": "What sweet natural liquid do worker honeybees gather from flowers?", "o": ["Nectar", "Pollen", "Sap", "Dew"], "a": 0, "c": "fun"},
  {"q": "Which tall mammal holds the record as the tallest living land animal?", "o": ["Giraffe", "African Elephant", "Camel", "Moose"], "a": 0, "c": "fun"},
  {"q": "In the video game Super Mario, what title profession is Mario?", "o": ["Plumber", "Carpenter", "Chef", "Doctor"], "a": 0, "c": "fun"},
  {"q": "What is the natural color of pure flamingo feathers before they eat shrimp?", "o": ["Grey / White", "Pink", "Red", "Yellow"], "a": 0, "c": "fun"},
]

# EBank (64 Bollywood and famous movies)
ebank = [
  {"e": "👨‍🎓 👨‍🎓 👨‍🎓 🏫 💡", "ans": "3 Idiots", "opts": ["3 Idiots", "Chhichhore", "Student of the Year", "Taare Zameen Par"]},
  {"e": "🤼‍♀️ 🥇 👨‍👧‍👧 🇮🇳", "ans": "Dangal", "opts": ["Dangal", "Sultan", "Mary Kom", "Chak De India"]},
  {"e": "👬 🔫 🪙 🚂", "ans": "Sholay", "opts": ["Sholay", "Deewaar", "Don", "Zanjeer"]},
  {"e": "🚆 🌾 🎻 👰", "ans": "Dilwale Dulhania Le Jayenge", "opts": ["Dilwale Dulhania Le Jayenge", "Kuch Kuch Hota Hai", "Kabhi Khushi Kabhie Gham", "Mohabbatein"]},
  {"e": "🛸 📻 🟡 👽", "ans": "PK", "opts": ["PK", "Koi Mil Gaya", "3 Idiots", "OMG"]},
  {"e": "⭐ 🎨 👦 👨‍🏫", "ans": "Taare Zameen Par", "opts": ["Taare Zameen Par", "Super 30", "Black", "Hichki"]},
  {"e": "🚂 ☕ 🥥 💃", "ans": "Chennai Express", "opts": ["Chennai Express", "Ra.One", "Happy New Year", "Dilwale"]},
  {"e": "⛏️ 💰 🧔 🔫", "ans": "KGF", "opts": ["KGF", "Pushpa", "Salaar", "Kantara"]},
  {"e": "🏍️ 🐎 🌊 🔥", "ans": "RRR", "opts": ["RRR", "Baahubali", "Magadheera", "Eega"]},
  {"e": "👶 🌊 🗡️ 👑", "ans": "Baahubali", "opts": ["Baahubali", "RRR", "Kantara", "Ponniyin Selvan"]},
  {"e": "🛸 👽 🏀 👓", "ans": "Koi Mil Gaya", "opts": ["Koi Mil Gaya", "Krrish", "PK", "Ra.One"]},
  {"e": "🪓 🌲 🚚 🧔", "ans": "Pushpa", "opts": ["Pushpa", "KGF", "Vikram", "Jailer"]},
  {"e": "🏏 🌧️ 💂‍♂️ 🌾", "ans": "Lagaan", "opts": ["Lagaan", "Chak De India", "83", "MS Dhoni"]},
  {"e": "🦸‍♂️ 🎭 ⚡ 🏙️", "ans": "Krrish", "opts": ["Krrish", "Ra.One", "Flying Jatt", "Bhavesh Joshi"]},
  {"e": "🚆 💔 🗣️ ❤️", "ans": "Jab We Met", "opts": ["Jab We Met", "Yeh Jawaani Hai Deewani", "Tamasha", "Highway"]},
  {"e": "👓 📞 💰 🐟", "ans": "Hera Pheri", "opts": ["Hera Pheri", "Phir Hera Pheri", "Welcome", "Golmaal"]},
  {"e": "👻 👗 🌙 ✂️", "ans": "Stree", "opts": ["Stree", "Bhool Bhulaiyaa", "Bhediya", "Roohi"]},
  {"e": "👮‍♂️ 🚂 🎭 💥", "ans": "Jawan", "opts": ["Jawan", "Pathaan", "War", "Fighter"]},
  {"e": "🐒 👧 🚂 🕊️", "ans": "Bajrangi Bhaijaan", "opts": ["Bajrangi Bhaijaan", "Tubelight", "Sultan", "Ek Tha Tiger"]},
  {"e": "🩺 👨‍⚕️ 🫂 🏥", "ans": "Munna Bhai M.B.B.S.", "opts": ["Munna Bhai M.B.B.S.", "Lage Raho Munna Bhai", "PK", "Sanju"]},
  {"e": "👻 🏰 💃 🗝️", "ans": "Bhool Bhulaiyaa", "opts": ["Bhool Bhulaiyaa", "Stree", "Bhootnath", "Pari"]},
  {"e": "🤪 🚗 🤣 👨‍👩‍👧‍👦", "ans": "Golmaal", "opts": ["Golmaal", "Dhamaal", "Housefull", "Fukrey"]},
  {"e": "🚗 🇪🇸 🤿 🍅", "ans": "Zindagi Na Milegi Dobara", "opts": ["Zindagi Na Milegi Dobara", "Dil Chahta Hai", "Yeh Jawaani Hai Deewani", "Tamasha"]},
  {"e": "🏑 🏆 🇮🇳 👩‍👩‍👧‍👦", "ans": "Chak De! India", "opts": ["Chak De! India", "Dangal", "Lagaan", "Mary Kom"]},
  {"e": "🛰️ 💧 💡 🚜", "ans": "Swades", "opts": ["Swades", "Lagaan", "Padman", "Pardes"]},
  {"e": "🩸 🩹 🚜 🧔", "ans": "Padman", "opts": ["Padman", "Toilet: Ek Prem Katha", "Special 26", "Airlift"]},
  {"e": "🚽 💒 💔 🏘️", "ans": "Toilet: Ek Prem Katha", "opts": ["Toilet: Ek Prem Katha", "Padman", "Panchayat", "Dum Laga Ke Haisha"]},
  {"e": "🍬 📻 🤫 🚲", "ans": "Barfi!", "opts": ["Barfi!", "Jagga Jasoos", "Tamasha", "Rockstar"]},
  {"e": "🎸 💔 🐦 🎤", "ans": "Rockstar", "opts": ["Rockstar", "Rock On", "Aashiqui 2", "Gully Boy"]},
  {"e": "🎤 🧢 🎙️ 🏙️", "ans": "Gully Boy", "opts": ["Gully Boy", "8 Mile", "Rockstar", "ABCD"]},
  {"e": "🐗 🔥 🪓 🌲", "ans": "Kantara", "opts": ["Kantara", "KGF", "Pushpa", "Baahubali"]},
  {"e": "⚔️ 🏴 🏰 🧔", "ans": "Salaar", "opts": ["Salaar", "KGF", "Pushpa", "Animal"]},
  {"e": "🪓 🧔 🩸 👨‍👦", "ans": "Animal", "opts": ["Animal", "Kabir Singh", "Arjun Reddy", "Sanju"]},
  {"e": "🩺 🏍️ 🕶️ 💔", "ans": "Kabir Singh", "opts": ["Kabir Singh", "Arjun Reddy", "Animal", "Aashiqui 2"]},
  {"e": "🏔️ 🎒 📸 💃", "ans": "Yeh Jawaani Hai Deewani", "opts": ["Yeh Jawaani Hai Deewani", "Tamasha", "Zindagi Na Milegi Dobara", "Jab We Met"]},
  {"e": "🎮 🤖 💙 ⚡", "ans": "Ra.One", "opts": ["Ra.One", "Robot / 2.0", "Krrish", "Flying Jatt"]},
  {"e": "🏍️ 👮 💨 💎", "ans": "Dhoom", "opts": ["Dhoom", "Don", "Race", "War"]},
  {"e": "🕶️ 🔫 ✈️ 💼", "ans": "Don", "opts": ["Don", "Dhoom", "War", "Pathaan"]},
  {"e": "💣 ❄️ 🚆 🪂", "ans": "Pathaan", "opts": ["Pathaan", "Jawan", "War", "Tiger 3"]},
  {"e": "✈️ 🥋 💥 🕺", "ans": "War", "opts": ["War", "Pathaan", "Bang Bang", "Fighter"]},
  {"e": "✈️ 🇮🇳 🚀 🛩️", "ans": "Fighter", "opts": ["Fighter", "Gunjan Saxena", "URI", "Border"]},
  {"e": "🪖 🇮🇳 💥 🚁", "ans": "URI: The Surgical Strike", "opts": ["URI: The Surgical Strike", "Border", "Shershaah", "Fighter"]},
  {"e": "🪖 🇮🇳 🏔️ 💔", "ans": "Shershaah", "opts": ["Shershaah", "URI", "Border", "LOC Kargil"]},
  {"e": "🚂 🚰 🇮🇳 🇵🇰", "ans": "Gadar", "opts": ["Gadar", "Gadar 2", "Border", "Bajrangi Bhaijaan"]},
  {"e": "🕷️ 🧑 🕸️ 🏙️", "ans": "Spider-Man", "opts": ["Spider-Man", "Batman", "Superman", "Iron Man"]},
  {"e": "🦸‍♂️ 🔨 🛡️ 🧤", "ans": "Avengers", "opts": ["Avengers", "Justice League", "Transformers", "Guardians of the Galaxy"]},
  {"e": "⚡ 🧙‍♂️ 🦉 🏰", "ans": "Harry Potter", "opts": ["Harry Potter", "Lord of the Rings", "Percy Jackson", "Chronicles of Narnia"]},
  {"e": "🦁 👑 🌅 🐗", "ans": "The Lion King", "opts": ["The Lion King", "Jungle Book", "Madagascar", "Tarzan"]},
  {"e": "🚢 🧊 🌊 💔", "ans": "Titanic", "opts": ["Titanic", "Life of Pi", "Cast Away", "Pirates of the Caribbean"]},
  {"e": "🦖 🚙 🏝️ 🧬", "ans": "Jurassic Park", "opts": ["Jurassic Park", "King Kong", "Godzilla", "Avatar"]},
  {"e": "🧊 👸 ⛄ ❄️", "ans": "Frozen", "opts": ["Frozen", "Tangled", "Moana", "Brave"]},
  {"e": "🤖 🕶️ 🦅 📱", "ans": "Robot / 2.0", "opts": ["Robot / 2.0", "Ra.One", "Krrish", "Terminator"]},
  {"e": "🌊 ⛵ 🌺 🏝️", "ans": "Moana", "opts": ["Moana", "Brave", "Tangled", "The Little Mermaid"]},
  {"e": "🍌 👓 🟡 🦹", "ans": "Despicable Me / Minions", "opts": ["Despicable Me / Minions", "Megamind", "The Incredibles", "Monsters Inc"]},
  {"e": "🦸‍♂️ 🦸‍♀️ 👶 🔥 💥", "ans": "The Incredibles", "opts": ["The Incredibles", "Fantastic Four", "Avengers", "Megamind"]},
  {"e": "💀 🎸 🏵️ 🇲🇽", "ans": "Coco", "opts": ["Coco", "Book of Life", "Soul", "Encanto"]},
  {"e": "👨‍🍳 🐀 🧀 🇫🇷", "ans": "Ratatouille", "opts": ["Ratatouille", "Chef", "Cloudy Meatballs", "Flushed Away"]},
  {"e": "🎈 🏠 👴 👦", "ans": "Up", "opts": ["Up", "Inside Out", "Wall-E", "Soul"]},
  {"e": "🧠 😢 😡 😄", "ans": "Inside Out", "opts": ["Inside Out", "Soul", "Up", "Coco"]},
  {"e": "🐼 🥋 🍜 🎋", "ans": "Kung Fu Panda", "opts": ["Kung Fu Panda", "Mulan", "Karate Kid", "Ninjago"]},
  {"e": "🐠 🔍 🌊 🦈", "ans": "Finding Nemo", "opts": ["Finding Nemo", "Shark Tale", "The Little Mermaid", "Moana"]},
  {"e": "🚗 🤖 💥 🛡️", "ans": "Transformers", "opts": ["Transformers", "Iron Man", "Real Steel", "Pacific Rim"]},
  {"e": "🦇 🃏 🏙️ 🚗", "ans": "The Dark Knight / Batman", "opts": ["The Dark Knight / Batman", "Spider-Man", "Superman", "Joker"]},
  {"e": "🏹 🍎 👸 🌲", "ans": "Brave", "opts": ["Brave", "Frozen", "Tangled", "Moana"]},
]

# RBank (100 Challenging Rapid Fire Questions)
rbank = [
  # SPORTS & CRICKET
  {"q": "In cricket, a batsman CANNOT be declared Out 'Hit the Ball Twice' if defending his wickets.", "a": True, "tag": "🏏 Cricket Rule"},
  {"q": "The official marathon race distance is exactly 42.195 kilometres (26.2 miles).", "a": True, "tag": "🏃 Sports"},
  {"q": "Neeraj Chopra threw over 90 metres when winning his Tokyo Olympic Gold medal.", "a": False, "tag": "🥇 Olympics"},
  {"q": "A standard Olympic swimming pool is 25 metres long.", "a": False, "tag": "🏊 Sports"},
  {"q": "Rohit Sharma is the only cricketer in world history to score 3 ODI double centuries.", "a": True, "tag": "🏏 Cricket"},
  {"q": "The 5 rings on the Olympic flag represent the 5 oceans of Earth.", "a": False, "tag": "🥇 Olympics"},
  {"q": "In Test cricket, Jasprit Bumrah once scored 35 runs in a single over off Stuart Broad.", "a": True, "tag": "🏏 Cricket Record"},
  {"q": "A standard tournament chess board contains a total of 64 individual squares.", "a": True, "tag": "♟️ Chess"},
  {"q": "Sunil Chhetri has scored more international football goals than Lionel Messi.", "a": False, "tag": "⚽ Football"},
  {"q": "Manu Bhaker became the first athlete of independent India to win 2 medals at a single Olympics.", "a": True, "tag": "🎯 Olympics 2024"},
  {"q": "In professional badminton, players must hit the shuttlecock from below 1.15 metres on a serve.", "a": True, "tag": "🏸 Badminton"},
  {"q": "India has won a total of 8 Olympic Gold medals in men's field hockey.", "a": True, "tag": "🏑 Hockey"},
  {"q": "A batsman can be given Out 'Stumped' on a Free Hit delivery in cricket.", "a": False, "tag": "🏏 Cricket"},
  {"q": "The Durand Cup is the oldest existing football tournament in Asia.", "a": True, "tag": "⚽ Football"},
  {"q": "Viswanathan Anand was the first recipient of the Khel Ratna award in India.", "a": True, "tag": "♟️ Chess & India"},
  {"q": "In cricket, if the ball strikes a fielder's helmet on the ground, 5 penalty runs are awarded.", "a": True, "tag": "🏏 Cricket Rule"},
  {"q": "Kolkata Knight Riders (KKR) won the IPL 2024 championship under Shreyas Iyer's captaincy.", "a": True, "tag": "🏏 IPL 2024"},
  {"q": "Football matches in standard FIFA competitions are played with 12 players per side on field.", "a": False, "tag": "⚽ Football"},
  {"q": "Virat Kohli was the player of the tournament in the ICC 2023 Men's Cricket World Cup.", "a": True, "tag": "🏏 Cricket"},
  {"q": "PV Sindhu is the only Indian woman athlete to win two individual Olympic medals.", "a": False, "tag": "🏸 Olympics"}, # Manu Bhaker also has 2!
  {"q": "A cricket pitch measures 22 yards (approximately 20.12 metres) between bowling creases.", "a": True, "tag": "🏏 Cricket Pitch"},
  {"q": "Sachin Tendulkar scored exactly 100 international centuries across Tests and ODIs.", "a": True, "tag": "🏏 Cricket Legend"},
  {"q": "The 2028 Summer Olympic Games will be hosted in Los Angeles, USA.", "a": True, "tag": "🥇 Future Games"},
  {"q": "In tennis, winning 4 consecutive Grand Slam tournaments in one calendar year is called a Calendar Grand Slam.", "a": True, "tag": "🎾 Tennis"},
  {"q": "Dhyan Chand scored over 400 international goals during his legendary hockey career.", "a": True, "tag": "🏑 Indian Legend"},

  # INDIA, POLITY & CURRENT AFFAIRS
  {"q": "Hindi is declared as the sole 'National Language' (Rashtrabhasha) in the Constitution of India.", "a": False, "tag": "🇮🇳 Constitution"},
  {"q": "The original Constitution of India was entirely handwritten, not typed or printed.", "a": True, "tag": "📜 Indian History"},
  {"q": "The Tropic of Cancer passes through exactly 8 Indian states.", "a": True, "tag": "🗺️ Geography"},
  {"q": "In Chandrayaan-3, the lander was named Pragyan and the rover was named Vikram.", "a": False, "tag": "🚀 ISRO Space"},
  {"q": "India's first satellite sent into space in 1975 was named Aryabhata.", "a": True, "tag": "🛰️ Space Science"},
  {"q": "The Reserve Bank of India (RBI) was founded before India achieved independence.", "a": True, "tag": "🏦 Indian Economy"},
  {"q": "The Preamble of the Indian Constitution has been amended multiple times in history.", "a": False, "tag": "🇮🇳 Constitution"},
  {"q": "The Bharat Ratna award has never been presented to any foreign citizen.", "a": False, "tag": "🏅 Honours"},
  {"q": "The Indian National Anthem 'Jana Gana Mana' was originally composed in Sanskrit.", "a": False, "tag": "🇮🇳 National Heritage"},
  {"q": "ISRO's Aditya-L1 spacecraft landed directly on the visible surface of the Sun.", "a": False, "tag": "☀️ ISRO Mission"},
  {"q": "The Lok Sabha chamber in India's new Parliament House is designed on a Peacock theme.", "a": True, "tag": "🏛️ Current Affairs"},
  {"q": "Indian Standard Time (IST) is exactly 5 hours and 30 minutes ahead of GMT.", "a": True, "tag": "⏰ World Time"},
  {"q": "Goa was liberated from Portuguese rule in 1947 together with mainland India.", "a": False, "tag": "📜 Indian History"},
  {"q": "Vande Bharat Express train rakes are manufactured at ICF Chennai.", "a": True, "tag": "🚆 Indian Railways"},
  {"q": "Mount Kanchenjunga is located on the boundary between Sikkim (India) and Nepal.", "a": True, "tag": "🏔️ Geography"},
  {"q": "The 24 spokes in the Ashoka Chakra represent the 24 hours of the day.", "a": True, "tag": "🇮🇳 National Flag"},
  {"q": "The national aquatic animal of India is the Ganges River Dolphin.", "a": True, "tag": "🐬 Wildlife"},
  {"q": "India has 28 States and 8 Union Territories.", "a": True, "tag": "🇮🇳 India Facts"},
  {"q": "Dr. APJ Abdul Kalam was the 11th President of the Republic of India.", "a": True, "tag": "🇮🇳 Presidents"},
  {"q": "Children's Day on November 14 marks Jawaharlal Nehru's birthday.", "a": True, "tag": "🎈 Children's Day"},
  {"q": "Sardar Vallabhbhai Patel is famously known as the 'Iron Man of India'.", "a": True, "tag": "🇮🇳 Leaders"},
  {"q": "The currency note of ₹2000 was officially withdrawn from circulation by RBI in 2023.", "a": True, "tag": "💰 Economy"},
  {"q": "India's highest civilian award is the Padma Vibhushan.", "a": False, "tag": "🏅 Honours"},
  {"q": "The Brahmaputra river enters India through the state of Arunachal Pradesh.", "a": True, "tag": "🌊 Indian Rivers"},
  {"q": "The Indian Tricolour flag ratio of width to length is strictly 2:3.", "a": True, "tag": "🇮🇳 Flag Code"},

  # SCIENCE & TECH TRICKY QUESTIONS
  {"q": "Light emitted from the Sun takes roughly 8 minutes and 20 seconds to reach Earth.", "a": True, "tag": "🌌 Astronomy"},
  {"q": "Glass is classified in physics and chemistry as an amorphous solid, often called a supercooled liquid.", "a": True, "tag": "🧪 Physics"},
  {"q": "One Gigabyte (GB) contains exactly 1,000 Megabytes (MB) in binary computation.", "a": False, "tag": "💻 Computers"},
  {"q": "Sound waves travel significantly faster through steel than through air.", "a": True, "tag": "🔊 Physics"},
  {"q": "Lightning bolts never strike the exact same spot on Earth twice.", "a": False, "tag": "⚡ Nature"},
  {"q": "In computer memory architecture, 1 Byte is composed of 16 bits.", "a": False, "tag": "💾 Computers"},
  {"q": "In mathematics, the number zero (0) is classified as an even integer.", "a": True, "tag": "📐 Mathematics"},
  {"q": "Earth's atmosphere is composed primarily of Oxygen gas (over 70%).", "a": False, "tag": "🌍 Atmosphere"},
  {"q": "Computer RAM keeps all its stored data intact even after power is completely cut off.", "a": False, "tag": "💻 Tech"},
  {"q": "Planet Venus rotates clockwise on its axis, opposite to most other planets.", "a": True, "tag": "🪐 Solar System"},
  {"q": "The Great Wall of China can be seen clearly from the Moon with unaided human eyes.", "a": False, "tag": "🌕 Space Fact"},
  {"q": "An octopus has three distinct hearts and blue-coloured blood.", "a": True, "tag": "🐙 Biology"},
  {"q": "Water expands in volume when it freezes into solid ice.", "a": True, "tag": "❄️ Chemistry"},
  {"q": "Tomatoes, cucumbers, and pumpkins are botanically classified as vegetables.", "a": False, "tag": "🍅 Botany"},
  {"q": "Bluetooth wireless technology was named after a 10th-century Scandinavian Viking King.", "a": True, "tag": "📱 Tech History"},
  {"q": "Fully electric vehicles (EVs) have zero exhaust tailpipe emissions during driving.", "a": True, "tag": "🚗 Modern Tech"},
  {"q": "Sharks have skeletons made of cartilage rather than true bones.", "a": True, "tag": "🦈 Marine Biology"},
  {"q": "Liquid nitrogen is colder than -190 degrees Celsius.", "a": True, "tag": "❄️ Science"},
  {"q": "Diamond and graphite in pencils are both made from the same element: Carbon.", "a": True, "tag": "💎 Chemistry"},
  {"q": "HTML is a computer programming language that performs mathematical calculations.", "a": False, "tag": "💻 Coding"},
  {"q": "Pure gold is 24 carats and is too soft for everyday gemstone jewellery.", "a": True, "tag": "💎 Minerals"},
  {"q": "Humans share approximately 60% of their DNA with bananas.", "a": True, "tag": "🧬 Genetics"},
  {"q": "The Sun constitutes more than 99% of all the mass in our solar system.", "a": True, "tag": "☀️ Solar System"},
  {"q": "A laser beam can travel infinitely without ever losing focus or intensity.", "a": False, "tag": "💡 Optics"},
  {"q": "Whales and dolphins are mammals and breathe atmospheric air through lungs.", "a": True, "tag": "🐋 Marine Life"},
  {"q": "Earth is physically closest to the Sun during the Northern Hemisphere winter (January).", "a": True, "tag": "🌍 Planetary Orbit"},
  {"q": "Pluto was reclassified by the International Astronomical Union as a dwarf planet in 2006.", "a": True, "tag": "🪐 Astronomy"},
  {"q": "Antibiotics are effective against both bacterial infections and common cold viruses.", "a": False, "tag": "💊 Medicine"},
  {"q": "The human stomach produces hydrochloric acid strong enough to dissolve zinc.", "a": True, "tag": "🧪 Human Body"},
  {"q": "Hot water can freeze faster than cold water under certain conditions (Mpemba effect).", "a": True, "tag": "❄️ Physics Curiosity"},

  # POP CULTURE, TRENDING & TRIVIA
  {"q": "MrBeast became the first individual YouTuber to reach 300 million subscribers.", "a": True, "tag": "📱 YouTube Trends"},
  {"q": "The popular video game GTA (Grand Theft Auto) is published by Rockstar Games.", "a": True, "tag": "🎮 Gaming"},
  {"q": "The symbol '@' was invented only after the internet was created in 1990.", "a": False, "tag": "⌨️ Typography"},
  {"q": "Subway Surfers was the most downloaded mobile game of the entire decade 2010–2019.", "a": True, "tag": "📱 Mobile Gaming"},
  {"q": "WhatsApp was acquired by Meta (Facebook) in 2014 for approximately $19 billion.", "a": True, "tag": "💼 Tech Business"},
  {"q": "Doraemon is a robotic cat from the 22nd century.", "a": True, "tag": "📺 Anime & Cartoons"},
  {"q": "Shah Rukh Khan's bungalow in Mumbai is officially named 'Mannat'.", "a": True, "tag": "🎬 Bollywood"},
  {"q": "Shinchan's pet white dog in the cartoon series is named Shiro.", "a": True, "tag": "📺 Cartoons"},
  {"q": "The movie 'Avatar' (2009) remains the highest-grossing film of all time worldwide.", "a": True, "tag": "🎬 Cinema Record"},
  {"q": "The song 'Naatu Naatu' from RRR won the Oscar for Best Original Song in 2023.", "a": True, "tag": "🏆 Oscar Winner"},
  {"q": "Instagram was originally launched exclusively for Apple iOS before coming to Android.", "a": True, "tag": "📱 App History"},
  {"q": "In the Marvel Cinematic Universe, Thor's original hammer is named Stormbreaker.", "a": False, "tag": "🦸 Marvel"}, # Original is Mjolnir!
  {"q": "Minecraft is currently the single best-selling video game of all time.", "a": True, "tag": "🎮 Gaming Record"},
  {"q": "Mickey Mouse originally made his first synchronized sound cartoon debut in 'Steamboat Willie'.", "a": True, "tag": "🐭 Animation History"},
  {"q": "The hashtag symbol '#' is also historically called an 'octothorpe'.", "a": True, "tag": "📱 Trivia"},
  {"q": "The viral AI chatbot ChatGPT reached 100 million active users in just 2 months.", "a": True, "tag": "🤖 AI Milestone"},
  {"q": "Chhota Bheem lives in the fictional kingdom named Dholakpur.", "a": True, "tag": "📺 Indian Cartoons"},
  {"q": "Bhaag Milkha Bhaag is a biographical sports film based on athlete Milkha Singh.", "a": True, "tag": "🎬 Bollywood"},
  {"q": "The official mascot of the Android mobile operating system is a green robot.", "a": True, "tag": "🤖 Android OS"},
  {"q": "Google was originally founded by Larry Page and Sergey Brin at Stanford University.", "a": True, "tag": "💻 Tech Giants"},
]

print(f"Total QBank: {len(qbank)}")
print(f"Total EBank: {len(ebank)}")
print(f"Total RBank: {len(rbank)}")

with open("game_template.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace QBank JSON
qbank_js = json.dumps(qbank, ensure_ascii=False, indent=2)
ebank_js = json.dumps(ebank, ensure_ascii=False, indent=2)
rbank_js = json.dumps(rbank, ensure_ascii=False, indent=2)

# Replace QBank
pattern_qbank = r"const QBank = \[[\s\S]*?\];\s*const catC"
replacement_qbank = f"const QBank = {qbank_js};\n    const catC"
html = re.sub(pattern_qbank, replacement_qbank, html, count=1)

# Replace EBank
pattern_ebank = r"const EBank=\[[\s\S]*?\];\s*let es=\{\};"
replacement_ebank = f"const EBank={ebank_js};\nlet es={{}};"
html = re.sub(pattern_ebank, replacement_ebank, html, count=1)

# Replace RBank
pattern_rbank = r"const RBank=\[[\s\S]*?\];\s*let rs=\{\};"
replacement_rbank = f"const RBank={rbank_js};\nlet rs={{}};"
html = re.sub(pattern_rbank, replacement_rbank, html, count=1)

# Add smart Deck Manager and update starter functions
smart_engine = """
// ========== SMART NON-REPEATING DECK ENGINE ==========
// Keeps track of unused questions across rounds so they never repeat until all are seen!
const Decks = {
  quiz: {},
  emoji: [],
  rapid: []
};

function getQuizSlice(cat, count = 10) {
  const full = cat === 'all' ? [...QBank] : QBank.filter(q => q.c === cat);
  if (!Decks.quiz[cat] || Decks.quiz[cat].length < count) {
    Decks.quiz[cat] = shuf(full);
  }
  const picked = Decks.quiz[cat].splice(0, count);
  // Ensure options inside each question are also shuffled freshly
  return picked.map(q => {
    const cor = q.o[q.a];
    const so = shuf([...q.o]);
    return { ...q, o: so, a: so.indexOf(cor) };
  });
}

function getEmojiSlice(count = 10) {
  if (!Decks.emoji || Decks.emoji.length < count) {
    Decks.emoji = shuf([...EBank]);
  }
  const picked = Decks.emoji.splice(0, count);
  return picked.map(q => {
    const so = shuf([...q.opts]);
    return { ...q, opts: so };
  });
}

function getRapidDeck() {
  if (!Decks.rapid || Decks.rapid.length < 35) {
    Decks.rapid = shuf([...RBank]);
  }
  // Take a fresh batch of 40 non-repeating questions
  const sliceCount = Math.min(40, Decks.rapid.length);
  return Decks.rapid.splice(0, sliceCount);
}

function startQuiz() {
  const cat = document.getElementById('qCat').value;
  const pool = getQuizSlice(cat, 10);
  qs = { pool, i: 0, sc: 0, timer: null };
  document.getElementById('qSetup').style.display = 'none';
  document.getElementById('qGame').style.display = 'block';
  document.getElementById('qEnd').style.display = 'none';
  showQ();
}

function startEmoji() {
  const pool = getEmojiSlice(10);
  es = { pool, i: 0, sc: 0, timer: null };
  document.getElementById('eSetup').style.display = 'none';
  document.getElementById('eGame').style.display = 'block';
  document.getElementById('eEnd').style.display = 'none';
  showE();
}

function startRapid() {
  const pool = getRapidDeck();
  rs = { pool, i: 0, ok: 0, no: 0, timer: null };
  document.getElementById('rSetup').style.display = 'none';
  document.getElementById('rGame').style.display = 'block';
  document.getElementById('rEnd').style.display = 'none';
  let tl = 60;
  document.getElementById('rTimer').textContent = '60';
  document.getElementById('rBar').style.width = '100%';
  document.getElementById('rTimer').style.color = 'var(--pink)';
  rs.timer = setInterval(() => {
    tl -= 0.1;
    if (tl <= 0) {
      clearInterval(rs.timer);
      endRapid();
      return;
    }
    document.getElementById('rTimer').textContent = Math.ceil(tl);
    document.getElementById('rBar').style.width = (tl / 60 * 100) + '%';
  }, 100);
  showR();
}
"""

# Replace existing startQuiz, startEmoji, startRapid
html = re.sub(r"function startQuiz\(\)\s*\{[\s\S]*?showQ\(\);\s*\}", "", html)
html = re.sub(r"function startEmoji\(\)\s*\{[\s\S]*?showE\(\)\}", "", html)
html = re.sub(r"function startRapid\(\)\s*\{[\s\S]*?showR\(\)\}", "", html)

# Insert smart_engine right before // ==================== QUIZ ====================
html = html.replace("// ==================== QUIZ ====================", smart_engine + "\n// ==================== QUIZ ====================")

with open("game_template.html", "w", encoding="utf-8") as f:
    f.write(html)

print("game_template.html updated successfully!")
