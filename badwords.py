
def get():
    words = ['condom', '4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass', 'ass-fucker', 'asses', 'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'ballbag', 'ballsack', 'bastard', 'beastial', 'beastiality', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bloody', 'blow job', 'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'breasts', 'buceta', 'bugger', 'bum', 'bunny fucker', 'butt', 'butthole', 'buttmuch', 'buttplug', 'c0ck', 'c0cksucker', 'carpet muncher', 'cawk', 'chink', 'cipa', 'cl1t', 'clit', 'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface', 'cockhead', 'cockmunch', 'cockmuncher', 'cocks', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cok', 'cokmuncher', 'coksucka', 'coon', 'cox', 'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot', 'cunilingus', 'cunillingus', 'cunnilingus', 'cunt', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cunts', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'dick', 'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin', 'dogging', 'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'f u c k', 'f u c k e r', 'f4nny', 'fag', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio', 'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks', 'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks', 'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fucker', 'fuckers', 'fuckhead', 'fuckheads', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucks', 'fuckwhit', 'fuckwit', 'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux', 'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged', 'gangbangs', 'gaylord', 'gaysex', 'goatse', 'hardcoresex', 'heshe', 'hoar', 'hoare', 'hoer', 'homo', 'hore', 'horniest', 'horny', 'hotsex', 'jack-off', 'jackoff', 'jap', 'jerk-off', 'jism', 'jiz', 'jizm', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'l3i+ch', 'l3itch', 'labia', 'lmfao', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist', 'master-bate', 'masterb8', 'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'numbnuts', 'nutsack', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'p0rn', 'pawn', 'pecker', 'penis', 'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'poop', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks', 'pron', 'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys', 'rectum', 'retard', 'rimjaw', 'rimming', 's hit', 's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum', 'semen', 'sex', 'sh!+', 'sh!t', 'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 'shemale', 'shi+', 'shit', 'shitdick', 'shite', 'shited', 'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting', 'shitings', 'shits', 'shitted', 'shitter', 'shitters', 'shitting', 'shittings', 'shitty', 'skank', 'slut', 'sluts', 'smegma', 'smut', 'snatch', 'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5', 't1tties', 'teets', 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'tittyfuck', 'tittywank', 'titwank', 'tosser', 'turd', 'tw4t', 'twat', 'twathead', 'twatty', 'twunt', 'twunter', 'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wanky', 'whoar', 'whore', 'willies', 'willy', 'xrated', 'xxx', 'abortion', 'abuse', 'addict', 'addicts', 'alligatorbait', 'amateursex', 'analannie', 'analsex', 'angie', 'areola', 'argie', 'aroused', 'arsehole', 'asian bitch', 'assassin', 'assassinate', 'assassination', 'assault', 'assbagger', 'assblaster', 'assclown', 'asscowboy', 'assfuck', 'asshat', 'asshore', 'assjockey', 'asskiss', 'asskisser', 'assklown', 'asslick', 'asslicker', 'asslover', 'assman', 'assmonkey', 'assmunch', 'assmuncher', 'asspacker', 'asspirate', 'asspuppies', 'assranger', 'asswhore', 'asswipe', 'athletesfoot', 'attack', 'australian', 'babe', 'babies', 'backdoor', 'backdoorman', 'backseat', 'badfuck', 'balllicker', 'banging', 'baptist', 'barelylegal', 'barf', 'barface', 'barfface', 'bast', 'bazongas', 'bazooms', 'beaner', 'beast', 'beastality', 'beatoff', 'beat-off', 'beatyourmeat', 'beaver', 'bi', 'bible', 'bicurious', 'bigass', 'bigbastard', 'bigbutt', 'bigger', 'bisexual', 'bi-sexual', 'bitchez', 'bitchslap', 'bitchy', 'biteme', 'black', 'blackman', 'blackout', 'blacks', 'blind', 'blow', 'boang', 'bogan', 'bohunk', 'bollick', 'bomb', 'bombers', 'bombing', 'bombs', 'bomd', 'bondage', 'bong', 'boobies', 'booby', 'boody', 'boom', 'boong', 'boonga', 'boonie', 'booty', 'bootycall', 'bountybar', 'bra', 'brea5t', 'breast', 'breastjob', 'breastlover', 'breastman', 'brothel', 'buggered', 'buggery', 'bullcrap', 'bulldike', 'bulldyke', 'bullshit', 'bumblefuck', 'bumfuck', 'bunga', 'bunghole', 'buried', 'burn', 'butchbabes', 'butchdike', 'butchdyke', 'buttbang', 'butt-bang', 'buttface', 'buttfuck', 'butt-fuck', 'buttfucker', 'butt-fucker', 'buttfuckers', 'butt-fuckers', 'butthead', 'buttman', 'buttmunch', 'buttmuncher', 'buttpirate', 'buttstain', 'byatch', 'cacker', 'cameljockey', 'cameltoe', 'canadian', 'cancer', 'carpetmuncher', 'carruth', 'catholic', 'catholics', 'cemetery', 'chav', 'cherrypopper', 'chickslick', "children's", 'chin', 'chinaman', 'chinamen', 'chinese', 'chinky', 'choad', 'chode', 'christ', 'christian', 'church', 'cigarette', 'cigs', 'clamdigger', 'clamdiver', 'clogwog', 'cocaine', 'cockblock', 'cockblocker', 'cockcowboy', 'cockfight', 'cockknob', 'cocklicker', 'cocklover', 'cocknob', 'cockqueen', 'cockrider', 'cocksman', 'cocksmith', 'cocksmoker', 'cocksucer', 'cock', 'cocktease', 'cocky', 'cohee', 'coitus', 'commie', 'communist', 'conservative', 'conspiracy', 'coolie', 'cooly', 'coondog', 'copulate', 'cornhole', 'corruption', 'cra5h', 'crackpipe', 'crackwhore', 'crack-whore', 'crapola', 'crapper', 'crappy', 'crash', 'creamy', 'crime', 'crimes', 'criminal', 'criminals', 'crotch', 'crotchjockey', 'crotchmonkey', 'crotchrot', 'cumbubble', 'cumfest', 'cumjockey', 'cumm', 'cumquat', 'cumqueen', 'cunn', 'cunntt', 'cunteyed', 'cuntfuck', 'cuntfucker', 'cuntsucker', 'cybersex', 'cyberslimer', 'dago', 'dahmer', 'dammit', 'damnation', 'damnit', 'darkie', 'darky', 'datnigga','deapthroat', 'deepthroat', 'defecate', 'dego', 'demon', 'deposit', 'desire', 'destroy', 'deth', 'devil', 'devilworshipper', 'dickbrain', 'dickforbrains', 'dickless', 'dicklick', 'dicklicker', 'dickman', 'dickwad', 'dickweed', 'diddle',dike', 'dingleberry', 'dipshit', 'dipstick', 'dirty', 'disease', 'dive', 'dix', 'dixiedike', 'dixiedyke', 'doggiestyle', 'doggystyle', 'dong', 'doodoo', 'doo-doo', 'doom', 'dope', 'dragqueen', 'dragqween', 'dripdick', 'drug', 'drunk', 'drunken', 'dumb', 'dumbass', 'dumbbitch', 'dumbfuck', 'dyefly', 'easyslut', 'eatballs', 'eatme', 'eatpussy', 'ecstacy', 'enema', 'enemy', 'erect', 'erection', 'ero', 'escort', 'ethiopian', 'evl', 'excrement', 'execute', 'executed', 'execution', 'executioner', 'explosion', 'facefucker', 'faeces', 'fart', 'farted', 'farting', 'farty', 'fastfuck', 'fatah', 'fatfuck', 'fatfucker', 'fatso', 'fckcum', 'felatio', 'felch', 'felcher', 'feltch', 'feltcher', 'feltching', 'fetish', 'fight', 'filipina', 'filipino', 'fingerfood','fister', 'fisting', 'flasher', 'flatulence', 'floo', 'flydie', 'flydye', 'fok', 'fondle', 'footaction', 'footfuck', 'footfucker', 'footlicker', 'footstar', 'fore', 'foreskin', 'forni', 'fornicate', 'foursome', 'fourtwenty', 'freakfuck', 'freakyfucker', 'freefuck', 'fu', 'fubar', 'fuc', 'fucck', 'fuckable', 'fuckbag', 'fuckbuddy', 'fuckedup', 'fuckface', 'fuckfest', 'fuckfreak', 'fuckfriend', 'fuckher', 'fuckina', 'fuckingbitch', 'fuckinnuts', 'fuckinright', 'fuckit', 'fuckknob', 'fuckmehard', 'fuckmonkey', 'fuckoff', 'fuckpig', 'fucktard', 'fuckwhore', 'fuckyou', 'fugly', 'funeral', 'funfuck', 'fungus', 'fuuck', 'gangbanger', 'gangsta', 'gatorbait', 'gay', 'gaymuthafuckinwhore', 'geez', 'geezer', 'geni', 'genital', 'getiton', 'gin', 'ginzo', 'gipp', 'girls', 'givehead', 'glazeddonut', 'gob', 'godammit', 'goddamit', 'goddammit', 'goddamnes', 'goddamnit', 'goddamnmuthafucker', 'goldenshower', 'gonorrehea', 'gonzagas', 'gook', 'gotohell', 'goy', 'goyim', 'greaseball', 'gringo', 'groe', 'gross', 'grostulation', 'gubba', 'gummer', 'gun', 'gyppie', 'gyppo', 'gyppy', 'hamas', 'handjob', 'hapa', 'harder', 'hardon', 'harem', 'headfuck', 'headlights', 'hebe', 'heeb', 'henhouse', 'heroin', 'herpes', 'heterosexual', 'hijack', 'hijacker', 'hijacking', 'hillbillies', 'hindoo', 'hiscock', 'hitler', 'hitlerism', 'hitlerist', 'hiv', 'hobo', 'hodgie', 'hoes', 'hole', 'holestuffer', 'homicide', 'homobangers', 'homosexual', 'honger', 'honk', 'honkers', 'honkey', 'honky', 'hook', 'hooker', 'hookers', 'hooters', 'hork', 'horn', 'horney', 'horseshit', 'hosejob', 'hoser', 'hostage', 'hotdamn', 'hotpussy', 'hottotrot', 'hummer', 'husky', 'hussy', 'hustler', 'hymen', 'hymie', 'iblowu', 'idiot', 'ikey', 'illegal', 'incest', 'insest', 'intercourse', 'interracial', 'intheass', 'inthebuff', 'israel', 'israeli', "israel's", 'italiano', 'itch', 'jackass', 'jackshit', 'jacktheripper', 'jade', 'japanese', 'japcrap', 'jebus', 'jeez', 'jerkoff', 'jesus', 'jesuschrist', 'jew', 'jewish', 'jiga', 'jigaboo', 'jigg', 'jigga', 'jiggabo', 'jigger', 'jiggy', 'jihad', 'jijjiboo', 'jimfish', 'jizim', 'jizjuice', 'jizzim', 'jizzum', 'joint', 'juggalo', 'jugs', 'junglebunny', 'kaffer', 'kaffir', 'kaffre', 'kafir', 'kanake', 'kid', 'kigger', 'kike', 'kill', 'killed', 'killer', 'killing', 'kills', 'kink', 'kinky', 'kissass', 'knife', 'knockers', 'koon', 'kotex', 'krap', 'krappy', 'kraut', 'kumbubble', 'kumbullbe', 'kumquat', 'kunnilingus', 'kunt', 'ky', 'kyke', 'lactate', 'laid', 'lapdance', 'latin', 'lesbain', 'lesbayn', 'lesbian', 'lesbin', 'lesbo', 'lez', 'lezbe', 'lezbefriends', 'lezbo', 'lezz', 'lezzo', 'liberal', 'libido', 'licker', 'lickme', 'lies', 'limey', 'limpdick', 'limy', 'lingerie', 'liquor', 'livesex', 'loadedgun', 'lolita', 'looser', 'loser', 'lotion', 'lovebone', 'lovegoo', 'lovegun', 'lovejuice', 'lovemuscle', 'lovepistol', 'loverocket', 'lowlife', 'lsd', 'lubejob', 'lucifer', 'luckycammeltoe', 'lugan', 'lynch', 'macaca', 'mad', 'mafia', 'magicwand', 'mams', 'manhater', 'manpaste', 'marijuana', 'mastabate', 'mastabater', 'masterblaster', 'mastrabator', 'masturbating', 'mattressprincess', 'meatbeatter', 'meatrack', 'meth', 'mexican', 'mgger', 'mggor', 'mickeyfinn', 'mideast', 'milf', 'minority', 'mockey', 'mockie', 'mocky', 'moky', 'moles', 'molest', 'molestation', 'molester', 'molestor', 'moneyshot', 'mooncricket', 'mormon', 'moron', 'moslem', 'mosshead', 'motherlovebone', 'muffdive', 'muffdiver', 'muffindiver', 'mufflikcer', 'mulatto', 'muncher', 'munt', 'murder', 'murderer', 'muslim', 'naked', 'narcotic', 'nasty', 'nastybitch', 'nastyho', 'nastyslut', 'nastywhore', 'necro', 'negro', 'negroes', 'negroid', "negro's", 'nig', 'niger', 'nigerian', 'nigerians', 'nigg', 'niggaracci', 'niggard', 'niggarded', 'niggarding', 'niggardliness', "niggardliness's", 'niggardly', 'niggards', "niggard's", 'niggerhead', 'niggerhole', "nigger's", 'niggle', 'niggled', 'niggles', 'niggling', 'nigglings', 'niggor', 'niggur', 'niglet', 'nignog', 'nigr', 'nigra', 'nigre', 'nip', 'nipple', 'nipplering', 'nittit', 'nlgger', 'nlggor', 'nofuckingway', 'nook', 'nookey', 'nookie', 'noonan', 'nooner', 'nude', 'nudger', 'nuke', 'nutfucker', 'nymph', 'ontherag', 'oral', 'orga', 'orgies', 'orgy', 'osama', 'paki', 'palesimian', 'palestinian', 'pansies', 'pansy', 'panti', 'panties', 'payo', 'pearlnecklace', 'peck', 'peckerwood', 'pee', 'peehole', 'pee-pee', 'peepshow', 'peepshpw', 'pendy', 'penetration', 'peni5', 'penile', 'penises', 'penthouse', 'perv', 'phungky', 'pi55', 'picaninny', 'piccaninny', 'pickaninny', 'piker', 'pikey', 'piky', 'pimp', 'pimped', 'pimper', 'pimpjuic', 'pimpjuice', 'pimpsimp', 'pindick', 'pisshead', 'pistol', 'pixie', 'pixy', 'playboy', 'playgirl', 'pocha', 'pocho', 'pocketpool', 'pohm', 'polack', 'pom', 'pommie', 'pommy', 'poo', 'poon', 'poontang', 'pooper', 'pooperscooper', 'pooping', 'poorwhitetrash', 'popimp', 'porchmonkey', 'pornflick', 'pornking', 'pornprincess', 'pot', 'poverty', 'premature', 'pric', 'prickhead', 'primetime', 'propaganda', 'pros', 'prostitute', 'protestant', 'pu55i', 'pu55y', 'pubic', 'pubiclice', 'pud', 'pudboy', 'pudd', 'puddboy', 'puke', 'puntang', 'purinapricness', 'puss', 'pussie', 'pussycat', 'pussyeater', 'pussyfucker', 'pussylicker', 'pussylips', 'pussylover', 'pussypounder', 'pusy', 'quashie', 'queef', 'queer', 'quickie', 'quim', 'ra8s', 'rabbi', 'racial', 'racist', 'radical', 'radicals', 'raghead', 'randy', 'rape', 'raped', 'raper', 'rapist', 'rearend', 'rearentry', 'redlight', 'redneck', 'reefer', 'reestie', 'refugee', 'reject', 'remains', 'rentafuck', 'republican', 'rere', 'retarded', 'ribbed', 'rigger', 'rimjob', 'roach', 'robber', 'roundeye', 'rump', 'russki', 'russkie', 'sadis', 'sadom', 'samckdaddy', 'sandm', 'sandnigger', 'satan', 'scag', 'scallywag', 'scat', 'screw', 'screwyou', 'scum', 'seppo', 'servant', 'sexed', 'sexfarm', 'sexhound', 'sexhouse', 'sexing', 'sexkitten', 'sexpot', 'sexslave', 'sextogo', 'sextoy', 'sextoys', 'sexual', 'sexually', 'sexwhore', 'sexy', 'sexymoma', 'sexy-slim', 'shat', 'shav', 'shawtypimp', 'sheeney', 'shhit', 'shinola', 'shitcan', 'shiteater', 'shitface', 'shitfaced', 'shitfit', 'shitforbrains', 'shitfucker', 'shithapens', 'shithappens', 'shithouse', 'shitlist', 'shitola', 'shitoutofluck', 'shitstain', 'shoot', 'shooting', 'shortfuck', 'showtime', 'sick', 'sissy', 'sixsixsix', 'sixtynine', 'sixtyniner', 'skankbitch', 'skankfuck', 'skankwhore', 'skanky', 'skankybitch', 'skankywhore', 'skinflute', 'skum', 'skumbag', 'slant', 'slanteye', 'slapper', 'slaughter', 'slav', 'slave', 'slavedriver', 'sleezebag', 'sleezeball', 'slideitin', 'slime', 'slimeball', 'slimebucket', 'slopehead', 'slopey', 'slopy', 'slutt', 'slutting', 'slutty', 'slutwear', 'slutwhore', 'smack', 'smackthemonkey', 'snatchpatch', 'snigger', 'sniggered', 'sniggering', 'sniggers', "snigger's", 'sniper', 'snot', 'snowback', 'snownigger', 'sob', 'sodom', 'sodomise', 'sodomite', 'sodomize', 'sodomy', 'sonofabitch', 'sonofbitch', 'sooty', 'sos', 'soviet', 'spaghettibender', 'spaghettinigger', 'spank', 'spankthemonkey', 'sperm', 'spermacide', 'spermbag', 'spermhearder', 'spermherder', 'spic', 'spick', 'spig', 'spigotty', 'spik', 'spit', 'spitter', 'splittail', 'spooge', 'spreadeagle', 'spunky', 'squaw', 'stagg', 'stiffy', 'strapon', 'stringer', 'stripclub', 'stroke', 'stroking', 'stupid', 'stupidfuck', 'stupidfucker', 'suck', 'suckdick', 'sucker', 'suckme', 'suckmyass', 'suckmydick', 'suckmytit', 'suckoff', 'suicide', 'swallow', 'swallower', 'swalow', 'swastika', 'sweetness', 'syphilis', 'taboo', 'taff', 'tampon', 'tang', 'tantra', 'tarbaby', 'tard', 'teat', 'terror', 'terrorist', 'teste', 'testicles', 'thicklips', 'thirdeye', 'thirdleg', 'threesome', 'threeway', 'timbernigger', 'tinkle', 'titbitnipply', 'titfucker', 'titfuckin', 'titjob', 'titlicker', 'titlover', 'tittie', 'titty', 'tnt','tongethruster', 'tonguethrust', 'tonguetramp', 'tortur', 'torture', 'towelhead', 'trailertrash', 'tramp', 'trannie', 'tranny', 'transexual', 'transsexual', 'transvestite', 'triplex', 'trisexual', 'trojan', 'trots', 'tuckahoe', 'tunneloflove', 'turnon', 'twink', 'twinkie', 'twobitwhore', 'uck','unfuckable', 'upskirt', 'uptheass', 'upthebutt', 'urinary', 'urinate', 'urine', 'usama', 'uterus', 'vaginal', 'vatican', 'vibr', 'vibrater', 'vibrator', 'vietcong', 'violence', 'virgin', 'virginbreaker', 'vomit', 'wab', 'wanking', 'waysted', 'weapon', 'weenie', 'weewee', 'welcher', 'welfare', 'wetb', 'wetback', 'wetspot', 'whacker', 'whash', 'whigger', 'whiskey', 'whiskeydick', 'whiskydick', 'whit', 'whitenigger', 'whitetrash', 'whitey', 'whiz', 'whop', 'whorefucker', 'whorehouse', 'wigger', 'willie', 'williewanker', 'wn', 'wog', "women's", 'wop', 'wtf', 'wuss', 'wuzzie', 'xtc', 'yankee', 'yellowman', 'zigabo', 'zipperhead', 'a55hole', 'aeolus', 'ahole', 'analprobe', 'anilingus', 'areole', 'arian', 'aryan', 'assbang', 'assbanged', 'assbangs', 'assh0le', 'assho1e', 'ass hole', 'assmaster', 'asswipes', 'azazel','babes', 'bang', 'banger', 'bastards', 'bawdy', 'beardedclam', 'beatch', 'beater', 'beer', 'beeyotch', 'beotch', 'bigtits', 'big tits', 'bimbo', 'bitched', 'bod', 'bodily', 'boink', 'bollocks', 'bone', 'boned', 'boners', 'booger', 'bookie', 'bootee', 'bootie', 'booze', 'boozer', 'boozy', 'bosom', 'bosomy', 'bowel', 'bowels', 'brassiere', 'bukkake', 'bull shit', 'bullshits', 'bullshitted', 'bullturds', 'bung', 'busty', 'butt fuck', 'c.0.c.k', 'c.o.c.k.', 'c.u.n.t', 'c-0-c-k', 'caca', 'cahone', 'cervix', 'chinc', 'chincs', 'chodes', 'climax', 'clitorus', 'clitty', 'cocain', 'c-o-c-k', 'cockholster', 'cockknocker', 'cock sucker', 'coital', 'coons', 'corksucker', 'cracker', 'cummin', 'cumshots', 'cumslut', 'cumstain', 'cunny', 'c-u-n-t', 'cuntface', 'cunthunter', 'd0ng', 'd0uch3', 'd0uche', 'd1ld0', 'd1ldo', 'dagos', 'damned', 'dawgie-style', 'dickbag', 'dickdipper', 'dickface', 'dickflipper', 'dickheads', 'dickish', 'dick-ish', 'dickripper', 'dicksipper', 'dickwhipper', 'dickzipper', 'diligaf', 'dillweed', 'dimwit', 'dingle', 'dipship', 'doggie-style', 'doggy-style', 'doofus', 'dopey', 'douch3', 'douche', 'douchebag', 'douchebags', 'douchey', 'dumass', 'dumbasses', 'dummy', 'dykes', 'enlargement', 'erotic', 'essohbee', 'extacy', 'extasy', 'f.u.c.k', 'fack', 'fagg', 'fagged', 'faggit', 'faig', 'faigt', 'fannybandit', 'fartknocker', 'fisted', 'fisty', 'floozy', 'foad', 'foobar', 'freex', 'frigg', 'frigga', 'f-u-c-k', 'fuckass', 'fucknugget', 'fucknut', 'fuck-tard', 'fuckup', 'fuckwad', 'fvck', 'fxck', 'gae', 'gai', 'ganja', 'gays', 'gey', 'gfy', 'ghay', 'ghey', 'gigolo', 'glans', 'godamn', 'godamnit', 'goddam', 'gonad', 'gonads', 'gooks', 'gspot', 'g-spot', 'gtfo', 'guido', 'h0m0', 'h0mo', 'hard on', 'he11', 'hemp', 'herp', 'herpy', 'hobag', 'hom0', 'homey', 'homoey', 'hooch', 'hookah', 'hoor', 'hootch', 'hooter', 'hump', 'humped', 'humping', 'inbred', 'injun', 'j3rk0ff', 'jackhole', 'japs', 'jerk', 'jerk0ff', 'jerked', 'jizzed', 'junkie', 'junky', 'kikes', 'klan', 'kooch', 'kooches', 'kootch', 'lech', 'leper', 'lesbians', 'lesbos', 'lezbian', 'lezbians', 'lezbos', 'lezzie', 'lezzies', 'lezzy', 'lmao', 'loin', 'loins', 'lube', 'lusty', 'massa', 'masterbating', 'masturbation', 'maxi', 'menses', 'menstruate', 'menstruation', 'm-fucking', 'moolie', 'motherfucka', 'mtherfucker', 'mthrfucker', 'mthrfucking', 'muthafuckaz', 'muthafucker', 'mutherfucking', 'muthrfucking', 'nad', 'nads', 'napalm', 'nappy', 'nazism', 'nimrod', 'ninny', 'nooky', 'nympho', 'opiate', 'opium', 'orally', 'organ', 'orgasmic', 'ovary', 'ovum', 'ovums', 'p.u.s.s.y.', 'paddy', 'pantie', 'panty', 'pastie', 'pasty', 'pcp', 'pedo', 'pedophile', 'pedophilia', 'pedophiliac', 'peepee', 'penetrate', 'penial', 'perversion', 'peyote', 'phalli', 'phallic', 'pillowbiter', 'pinko', 'piss-off', 'pms', 'pollock', 'potty', 'prig', 'prude', 'pubis', 'punkass', 'punky', 'puto', 'queaf', 'queero', 'queers', 'quicky', 'racy', 'raunch', 'rectal', 'rectus', 'reetard', 'reich', 'revue', 'ritard', 'rtard', 'r-tard', 'rum', 'rumprammer', 'ruski', 's.h.i.t.', 's0b', 'sadism', 'scantily', 'schizo', 'screwed', 'scrog', 'scrot', 'scrud', 'seaman', 'seamen', 'seduce', 's-h-1-t', 'shamedame', 's-h-i-t', 'shithole', 'shitt', 'shiz', 'skag', 'sleaze', 'sleazy', 'slutdumper', 'slutkiss', 'smutty', 'snuff', 's-o-b', 'souse', 'soused', 'spiks', 'steamy', 'stfu', 'stoned', 'strip', 'sucked', 'sucking', 'sumofabiatch', 't1t', 'tawdry', 'teabagging', 'terd', 'testee', 'testes', 'testis', 'thrust', 'thug', 'titi', 'tittyfucker', 'toke', 'toots', 'trashy', 'tubgirl', 'tush', 'twats', 'ugly', 'undies', 'unwed', 'urinal', 'uzi', 'vag', 'valium', 'vixen', 'vodka', 'voyeur', 'vulgar', 'wad', 'wazoo', 'wedgie', 'weed', 'weiner', 'weirdo', 'wench', 'wh0re', 'wh0reface', 'whoralicious', 'whorealicious', 'whored', 'whoreface', 'whorehopper', 'whores', 'whoring', 'womb', 'woody', 'x-rated', 'yeasty', 'yobbo', 'zoophile', 'ass lick', 'beastility', 'belly whacker', 'bonehead', 'browntown', 'bucket cunt', 'bung hole', 'butch', 'butt breath', 'butt fucker', 'butt hair', 'buttpicker', 'circle jerk', 'clam', 'cobia', 'cooter', 'douche bag', 'fagget', 'fartings', 'farts', 'furburger', 'gazongers', 'guinne', 'jack off', 'jacking off', 'jesus christ', 'merde', 'mick', 'mound','round ass',punk', 'sheister'
    ]
    return words