import requests
lis = [
    {
        "sku": "ANDO1549",
        "product_name": "Smith Armchair",
        "product_description": "Neutral upholstery and subtle tufting make this charming arm chair the perfect anchor for your master suite or living room. Top it with a velvet throw and Damask pillow for a touch of sophisticated style, or keep it casual with a cozy wool throw and solid pillow.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-smith-armchair-ando1549.html",
        "class_name": "Accent Chairs",
        "sale_price": 179.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30808/15664008/1/Ogelthrope%2BXpress%2BChair.jpg",
        "model": {
            "dimensions_inches": {
                "x": 34,
                "y": 33,
                "z": 35
            },
            "glb": "http://img.wfrcdn.com/docresources/30808/107/1071266.glb",
            "obj": "http://img.wfrcdn.com/docresources/30808/76/762991.zip"
        }
    },
    {
        "sku": "ANDO1569",
        "product_name": "Dewitt Barrel Side Chair",
        "product_description": "This barrel side chair is the perfect seating addition to your home. Just add it to your living room, entertainment room, or even a children’s play room for an added seat that is able to support up to 250 lbs. Child friendly, this piece is easily cleaned with soap and water. Measuring 38'' H x 46'' W x 44'' D, this rounded back chair is upholstered with a polyester blend and filled with foam. Easily assembled with detachable legs.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-dewitt-barrel-side-chair-ando1569.html",
        "class_name": "Accent Chairs",
        "sale_price": 369.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/59407815/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 46,
                "y": 44,
                "z": 38
            },
            "glb": "http://img.wfrcdn.com/docresources/30808/118/1180601.glb",
            "obj": "http://img.wfrcdn.com/docresources/30808/118/1185304.zip"
        }
    },
    {
        "sku": "CSTD2801",
        "product_name": "Marta Armchair",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/corrigan-studio-marta-armchair-cstd2801.html",
        "class_name": "Accent Chairs",
        "sale_price": 359.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36990/33486437/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 26,
                "y": 21.9,
                "z": 32.3
            },
            "glb": "http://img.wfrcdn.com/docresources/36990/109/1091009.glb",
            "obj": "http://img.wfrcdn.com/docresources/36990/105/1050153.zip"
        }
    },
    {
        "sku": "FV50959",
        "product_name": "Natuna Armchair",
        "product_description": "Crafted of Kubu gray rattan which is coveted for its natural soft grey color, the Natuna Armchair is easy and breezy year round. With its artfully woven sculptural lines, this transitional chair is chic and comfortable in the family room or dining room.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/safavieh-natuna-armchair-fv50959.html",
        "class_name": "Accent Chairs",
        "sale_price": 259.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/428/12618121/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 25.64,
                "y": 25.31,
                "z": 35.35
            },
            "glb": "http://img.wfrcdn.com/docresources/428/107/1073540.glb",
            "obj": "http://img.wfrcdn.com/docresources/428/88/885210.zip"
        }
    },
    {
        "sku": "GOLV5061",
        "product_name": "Oxendine Traditional Fabric Armchair",
        "product_description": "This Oxendine Traditional Fabric Club Chair is a great addition to any room in your home. Featuring an extra cushioned seat and backrest along with lightly cushioned armrests, this chair is sure to be a favorite amongst the family.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/george-oliver-oxendine-traditional-fabric-armchair-golv5061.html",
        "class_name": "Accent Chairs",
        "sale_price": 315.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/44308/58627652/1/furniture%2Fpdp%2Fgeorge-oliver-oxendine-traditional-fabric-armchair.jpg",
        "model": {
            "dimensions_inches": {
                "x": 28.25,
                "y": 31.49,
                "z": 32.75
            },
            "glb": "http://img.wfrcdn.com/docresources/44316/130/1303267.glb",
            "obj": "http://img.wfrcdn.com/docresources/44316/130/1308406.zip"
        }
    },
    {
        "sku": "LATR7704",
        "product_name": "Microscopium Barrel Chair",
        "product_description": "Pairing a swivel design with a silhouette, this distinctive barrel chair is sure to spark conversation in your favorite seating space. Its nailhead trim adds a timeless touch to your decor while its solid pattern blends effortlessly into monochromatic and vibrant palettes. Play into this piece's contemporary influence by adding it to a living room seating group comprised of a mid-century-inspired loveseat and streamlined sofa for a complementing look, then accent the arrangement with an embroidered patchwork pillow for a touch of texture. Build up the aesthetic by dotting nearby walls with beveled oval mirrors and black-and-white cityscape photographs for an eye-catching display, then pair it with hanging woven tapestry for an unexpected dash of drama. Whether you're seating guests at your next neighborhood get-together or enjoying weekend movie night, this polyester-upholstered chair is a perfect addition to your favorite aesthetic.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/latitude-run-microscopium-barrel-chair-latr7704.html",
        "class_name": "Accent Chairs",
        "sale_price": 332.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/40128/35834628/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 26.9,
                "y": 25.73,
                "z": 27.21
            },
            "glb": "http://img.wfrcdn.com/docresources/40128/107/1072184.glb",
            "obj": "http://img.wfrcdn.com/docresources/40128/76/763964.zip"
        }
    },
    {
        "sku": "LATR8439",
        "product_name": "Dorset Barrel Chair",
        "product_description": "Understated with a rounded silhouette, this barrel chair works wonderfully in both classic and contemporary ensembles. Its frame is crafted of birch wood, featuring a four-leg foundation with a dark brown finish. Its seat is topped off by a single cushion stuffed with medium-firm polyester fill, while the upholstery wraps around the rest in a versatile solid hue. Assembly is easy with only the legs needing to be attached once it arrives.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/latitude-run-dorset-barrel-chair-latr8439.html",
        "class_name": "Accent Chairs",
        "sale_price": 207.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/60043469/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 29.09,
                "y": 29.89,
                "z": 29.54
            },
            "glb": "http://img.wfrcdn.com/docresources/40128/115/1159971.glb",
            "obj": "http://img.wfrcdn.com/docresources/40128/117/1175073.zip"
        }
    },
    {
        "sku": "LGLY3906",
        "product_name": "Birmingham Armchair",
        "product_description": "This wood frame arm chair combines a classic French-style with a bold look that will compliment any decor. Well-padded on the back and seat and includes an additional throw pillow for style and added comfort.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-birmingham-armchair-lgly3906.html",
        "class_name": "Accent Chairs",
        "sale_price": 275.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36991/33501240/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 24.7,
                "y": 28.7,
                "z": 32
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/115/1156128.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/116/1168126.zip"
        }
    },
    {
        "sku": "LRFY4876",
        "product_name": "Haywood Swivel Barrel Chair",
        "product_description": "Pairing a floral paisley pattern with neutral hues, this swivel arm chair adds a refined touch to any seating group. Its distressed details pair perfectly with antiqued decor and weathered accents while its understated deign fits aesthetics from cottage-chic to crisp contemporary. Add this option to the den to complement a farmhouse arrangement or use it to level out a breezy coastal look in the living room. Try draping a cable-knit throw over its back for a casual display, or pair it with a patchwork pillow for a bold pop of pattern. Use this design to seat guests at your next neighborhood get-together, or to curl up and watch the big game with your favorite beverage. Its solid birch-wood frame gives it a sturdy foundation while its barrel silhouette adds a refined touch to any space. With its garden-chic motif and rolled arms, this eye-catching design is the perfect finishing touch to your cozy home.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/haywood-swivel-barrel-chair-lrfy4876.html",
        "class_name": "Accent Chairs",
        "sale_price": 374,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/42526/37202443/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 32.22,
                "y": 30.44,
                "z": 31.99
            },
            "glb": "http://img.wfrcdn.com/docresources/42526/131/1316702.glb",
            "obj": "http://img.wfrcdn.com/docresources/42526/132/1329393.zip"
        }
    },
    {
        "sku": "MCRW1865",
        "product_name": "Quinten Slipper Chair",
        "product_description": "Add a splash of streamlined style to your seating group with this slipper chair. Crafted with a solid birch frame, this piece is filled with foam for a medium firm feel. Its poly-blend upholstery is offered in a variety of tones to ensure it suits your color palette, while its single row of button-tufted details lend the solid-hued seat a touch of texture. Four amber-finished legs give it a bit of warmth and round out this design.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercury-row-quinten-slipper-chair-mcrw1865.html",
        "class_name": "Accent Chairs",
        "sale_price": 175.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58387287/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 24.89,
                "y": 31.29,
                "z": 31.46
            },
            "glb": "http://img.wfrcdn.com/docresources/33808/119/1195198.glb",
            "obj": "http://img.wfrcdn.com/docresources/33808/121/1212181.zip"
        }
    },
    {
        "sku": "MCRW6355",
        "product_name": "Derrico Armchair",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercury-row-derrico-armchair-mcrw6355.html",
        "class_name": "Accent Chairs",
        "sale_price": 319.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/29633/58012654/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 22.1,
                "y": 28.44,
                "z": 34.51
            },
            "glb": "http://img.wfrcdn.com/docresources/33808/128/1284223.glb",
            "obj": "http://img.wfrcdn.com/docresources/33808/129/1290414.zip"
        }
    },
    {
        "sku": "ONAW2547",
        "product_name": "Yerres Wingback Chair",
        "product_description": "This chair is a tribute to the elegance of styles from the past gentle curves, button tufting and a hand finished frame. Add a touch of sophistication to your bedroom or living room with this chair.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/one-allium-way-yerres-wingback-chair-onaw2547.html",
        "class_name": "Accent Chairs",
        "sale_price": 459.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2418/41010755/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 29.31,
                "y": 29.96,
                "z": 39.33
            },
            "glb": "http://img.wfrcdn.com/docresources/37307/112/1123731.glb",
            "obj": "http://img.wfrcdn.com/docresources/37307/114/1140683.zip"
        }
    },
    {
        "sku": "RDBS1728",
        "product_name": "Yellowstone Valley Contemporary Armchair",
        "product_description": "Sleek design and superior comfort makes this piece an obvious favorite among family and friends. Sure to have guests arriving unannounced to enjoy the lux softness of this chair, your popularity just got a boost! Upholstered in a patterned fabric, the high-density foam filled cushion is conveniently removable for lasting use. Perfectly stitched, this chair is complete with padded arm rest.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/red-barrel-studio-yellowstone-valley-contemporary-armchair-rdbs1728.html",
        "class_name": "Accent Chairs",
        "sale_price": 1169.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/34591/27298218/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 36.58,
                "y": 37.01,
                "z": 45.29
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/109/1090515.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/101/1016208.zip"
        }
    },
    {
        "sku": "SEHO1600",
        "product_name": "Randall Armchair",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/beachcrest-home-randall-armchair-seho1600.html",
        "class_name": "Accent Chairs",
        "sale_price": 323.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37308/39048857/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 28.7,
                "y": 32.98,
                "z": 31.42
            },
            "glb": "http://img.wfrcdn.com/docresources/37308/119/1199943.glb",
            "obj": "http://img.wfrcdn.com/docresources/37308/121/1215153.zip"
        }
    },
    {
        "sku": "VKGL1857",
        "product_name": "Potts Barrel Chair",
        "product_description": "Sit pretty or simply add high style to your space with this beautiful barrel chair. Crafted of wood, this delightful design is founded on a four leg tapered base with a dramatically curved top silhouette. Contemporary but still comfortable, it is wrapped in glossy leather-inspired upholstery with a solid hue for a more versatile look. Set it in the den along with a clean-lined love seat for a chic seating group, then roll out a trellis-printed rug on the floor below, use a sleek coffee table to display a trio of earthy succulents, and suspend an exposed light bulb overhead to really make it shine.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/wrought-studio-potts-barrel-chair-vkgl1857.html",
        "class_name": "Accent Chairs",
        "sale_price": 169.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36987/27237285/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 30.69,
                "y": 27.46,
                "z": 32.16
            },
            "glb": "http://img.wfrcdn.com/docresources/36987/128/1280966.glb",
            "obj": "http://img.wfrcdn.com/docresources/36987/128/1285254.zip"
        }
    },
    {
        "sku": "WADL4889",
        "product_name": "Evanston Chair in White",
        "product_description": "Quintessentially contemporary, the Faux Leather Barrel Chair is perfect to keep in your living room, home library, or study room. Simply designed to offer efficacy, this barrel chair has a sleek style that is hard to miss. It has immaculate lines and meticulous cuts, which are further enhanced by its flawless finesse. Offering a fine blend of style and efficacy, this barrel chair can also be used in the office, restaurant, or any other commercial place.  The Faux Leather Barrel Chair is made from a stainless steel frame for unrivaled strength and sturdiness. It has a foam-filled seat, which is soft to touch and comfortable to sit for a long time. This barrel chair is upholstered in white faux leather, which perfectly complements the chrome-finished steel frame. It has flared arms and a sturdy pedestal base that facilitates good balance on the floor. This barrel chair has a capacity of 250 pounds, and comes with a removable seat cushion for hassle-free cleaning.   This barrel chair requires minimal assembly, and can be easily put together using simple household tools. Low on maintenance, this leather chair can be occasionally cleaned using mild leather cleaner.  ",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/wade-logan-evanston-chair-in-white-wadl4889.html",
        "class_name": "Accent Chairs",
        "sale_price": 180.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/59140456/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 29.2,
                "y": 26.44,
                "z": 31.98
            },
            "glb": "http://img.wfrcdn.com/docresources/36989/129/1293304.glb",
            "obj": "http://img.wfrcdn.com/docresources/36989/129/1296618.zip"
        }
    },
    {
        "sku": "WADL9371",
        "product_name": "Ares Armchair",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/wade-logan-ares-armchair-wadl9371.html",
        "class_name": "Accent Chairs",
        "sale_price": 335.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58566361/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 29.74,
                "y": 33.43,
                "z": 33.08
            },
            "glb": "http://img.wfrcdn.com/docresources/36989/124/1244612.glb",
            "obj": "http://img.wfrcdn.com/docresources/36989/125/1254567.zip"
        }
    },
    {
        "sku": "WDLN3255",
        "product_name": "Alfredo Leisure Lounge Chair",
        "product_description": "The high-style, retro chic design is not to be ignored. Inspired by the designs of Arne Emil Jacobson, this collection is a sculptural masterpiece; specifically designed to maximize comfort, while maintaining an unobtrusive profile. Hand-sewn with the finest fabric, and standing on a pedestal of chrome cross legs, this collection is a true work of art that is sure to pop in any decor.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/wade-logan-alfredo-leisure-lounge-chair-wdln3255.html",
        "class_name": "Accent Chairs",
        "sale_price": 263.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/55064355/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 28.7,
                "y": 24.8,
                "z": 35
            },
            "glb": "http://img.wfrcdn.com/docresources/36989/117/1173534.glb",
            "obj": "http://img.wfrcdn.com/docresources/36989/118/1183086.zip"
        }
    },
    {
        "sku": "ZIPC4121",
        "product_name": "Liam Barrel Chair",
        "product_description": "<i>Mooove</i> on over to make room for your new favorite accent chair! This American-made design brings a little down-home flair to any seating arrangement, combining a cowhide pattern with a classic silhouette to create a piece that pairs well with both contemporary and rustic ensembles. Founded atop four tapered legs, its manufactured wood frame is wrapped in polyester blend fabric that’s easy to keep pristine. Measuring 32'' H x 30.5'' W x 27.5'' D.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-liam-barrel-chair-zipc4121.html",
        "class_name": "Accent Chairs",
        "sale_price": 172.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/59803713/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 34.29,
                "y": 27.86,
                "z": 32.46
            },
            "glb": "http://img.wfrcdn.com/docresources/37311/108/1089869.glb",
            "obj": "http://img.wfrcdn.com/docresources/37311/101/1014484.zip"
        }
    },
    {
        "sku": "ZIPC6590",
        "product_name": "Weymand Floral Slipper Chair",
        "product_description": "Why let your garden get all the glory? You can instantly add a little blooming beauty into your bedroom with this stunning slipper chair. Simply set it in a sunny corner for a posh spot to unwind with your latest read, or try pulling up an end table topped with a mirror and essential cosmetics to craft an impromptu vanity display. Founded atop four gently tapered legs finished in espresso, its clean-lined frame is crafted of solid wood and wrapped in floral-printed cotton upholstery. For a more lively living room look, try pulling it up beside a neutral loveseat for an instant pop of pattern. To tie it all together in your own style, just roll out a flat-woven rug on the floor below, hang up flowing sheer curtains, and set out a glossy white coffee table topped with a trio of lush succulents. Though this distinctive design is certainly striking solo, you can lend a little extra luxury by tossing a lush shag throw over the back.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-weymand-floral-slipper-chair-zipc6590.html",
        "class_name": "Accent Chairs",
        "sale_price": 141.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/30593/61603901/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 22,
                "y": 29.74,
                "z": 33
            },
            "glb": "http://img.wfrcdn.com/docresources/0/139/1396770.glb",
            "obj": "http://img.wfrcdn.com/docresources/0/139/1396771.zip"
        }
    },
    {
        "sku": "ALTL1608",
        "product_name": "Groveland Navy Indoor/Outdoor Area Rug",
        "product_description": "This delightful collection of quality loomed rugs provides an instant housewarming. Choose from an exciting array of foliage and flower based designs, some with bold interplays of curvaceous geometrics. Conceived in deeply pigmented tones that contrast beautifully with soft neutrals, for an effect as lush and welcoming as a sultry island garden. The woven loop pile adds an appealing accent of visual and tactile texture.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/alcott-hill-groveland-navy-indooroutdoor-area-rug-altl1608.html",
        "class_name": "Area Rugs",
        "sale_price": 53.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36985/61826565/1/rugs%2Fpdp%2Falcott-hill-groveland-navy-indooroutdoor-area-rug.jpg",
        "model": {
            "dimensions_inches": {
                "x": 63,
                "y": 89,
                "z": 0.5
            },
            "glb": "http://img.wfrcdn.com/docresources/36985/107/1072374.glb",
            "obj": "http://img.wfrcdn.com/docresources/36985/75/753376.zip"
        }
    },
    {
        "sku": "ANDO3516",
        "product_name": "Virginia Beige/Red Area Rug",
        "product_description": "Put the focus on your floor and anchor any ensemble in your home with classic sophistication when you roll out this charming rug. Brimming with traditional elegance, it will effortlessly elevate your aesthetic. The paisley-inspired botanical pattern gives this rug floral fancy and eye-catching appeal, while the red, green and orange color palette and the solid-toned background adds refined style. Try rolling this rug out in your foyer to greet guests with welcoming style, then complement the botanical print by dotting the walls with framed floral art. If you want to give your whole space a refresh, start by adding a simple gray linen bench and an oak-finished coffee table, then top the table with a stack of glossy fashion books, a trio of golden candlesticks and a blooming bouquet of flowers from your backyard garden for a dazzling display that is sure to impress.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/andover-mills-virginia-beigered-area-rug-ando3516.html",
        "class_name": "Area Rugs",
        "sale_price": 33.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30808/34906844/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 60,
                "y": 96,
                "z": 0.44
            },
            "glb": "http://img.wfrcdn.com/docresources/30808/107/1072416.glb",
            "obj": "http://img.wfrcdn.com/docresources/30808/76/764264.zip"
        }
    },
    {
        "sku": "ANDO4524",
        "product_name": "Raffin Beige/Brown Leaves Area Rug",
        "product_description": "Instantly elevate your floors in understated elegance with this eye-catching rug, crafted from polypropylene. Its floral details add botanical charm to any space while its muted colors pair perfectly against a hardwood floor for a complementing look. Play up this piece's traditional influence by adding it to a entryway alongside a cherry-finished console table, topped with a trio of turned candleholders for a dash of dimension. Adorn nearby walls with equestrian canvas prints and typographic decor for an eye-catching display, then suspend a geometric pendant above the space to illuminate your room in visual appeal. With its floral motif and geometric details, this lovely rug is the perfect option for anchoring high traffic areas in the living room, or defining space in the den.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/andover-mills-raffin-beigebrown-leaves-area-rug-ando4524.html",
        "class_name": "Area Rugs",
        "sale_price": 11.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30808/58055036/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 108,
                "y": 79,
                "z": 0.5
            },
            "glb": "http://img.wfrcdn.com/docresources/30808/107/1072499.glb",
            "obj": "http://img.wfrcdn.com/docresources/30808/76/764335.zip"
        }
    },
    {
        "sku": "ANDO4889",
        "product_name": "Smithtown Area Rug",
        "product_description": "Sophisticated color and incomparable texture in a unique collection of high fashion accent and area rugs. Made exclusively from unique fiber for superlative softness and durability. Expertly woven on state-of-the-art Wilton looms. A wealth of fashion-forward color palettes warmly enhanced by the rich patina of the special proprietary fiber. Specially dyed yarns create a shaded “abrash” effect that evokes the vintage appeal of the finest handmade carpets. Subtle accents of hand carving impart an elegant sense of dimension to the feature elements of each signature design.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/andover-mills-smithtown-area-rug-ando4889.html",
        "class_name": "Area Rugs",
        "sale_price": 35.51,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/56764884/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 63,
                "y": 89,
                "z": 0.5
            },
            "glb": "http://img.wfrcdn.com/docresources/30808/109/1096723.glb",
            "obj": "http://img.wfrcdn.com/docresources/30808/105/1050634.zip"
        }
    },
    {
        "sku": "BGLS4809",
        "product_name": "Indira Gray & Light Blue Area Rug",
        "product_description": "Set a fashionable foundation in any space with this area rug, showcasing an abstract pattern in neutral gray and taupe tones with pops of light blue for a subtle splash of color. Power-loomed in Turkey from polypropylene, this durable design is an ideal option for busy entryways, bustling living rooms, or any other high-traffic room in your home. Though its medium 0.45\" pile height provides a bit of padding underfoot, this piece is best paired with a rug pad for extra cushioning and traction.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/bungalow-rose-annabel-gray-light-blue-area-rug-w000660168.html",
        "class_name": "Area Rugs",
        "sale_price": 37.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37700/34722173/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 96.01,
                "y": 132.01,
                "z": 0.51
            },
            "glb": "http://img.wfrcdn.com/docresources/37700/109/1099139.glb",
            "obj": "http://img.wfrcdn.com/docresources/37700/109/1099140.zip"
        }
    },
    {
        "sku": "LATR7331",
        "product_name": "Myia Radiance Area Rug",
        "product_description": "Like sprinkles of lush leaves falling softly over water, the design of the radiance style was inspired by nature’s splendor. Cool aqua shades run alongside hints of chartreuse, sky blue and rich gray in the palette of the Radiance. This rug is quality constructed with Latitude Run exclusive wear dated nylon, designed specifically to resist staining and crushing in high traffic areas of the home.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/latitude-run-myia-radiance-area-rug-latr7331.html",
        "class_name": "Area Rugs",
        "sale_price": 52.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/40128/57066735/1/rugs%2Fpdp%2Flatitude-run-myia-radiance-area-rug.jpg",
        "model": {
            "dimensions_inches": {
                "x": 60.05,
                "y": 96.05,
                "z": 0.43
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/118/1183841.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/118/1189812.zip"
        }
    },
    {
        "sku": "MCRR7867",
        "product_name": "Marcelo Hand Woven Ivory Area Rug",
        "product_description": "Take any floor space from dull to dazzling with this chic area rug. Crafted in India, it is hand woven of 80% wool and 20% cotton and features canvas backing. Printed with a diamond motif in versatile this rug is perfect adding a pop of pattern to any ensemble. Let it sit below a pair of crisp white love seats to craft an elegant living room ensemble, or have it anchor a streamlined dining set to refresh your entertaining space. It's also the perfect foundation for your eye-catching entryway ensemble; Just add in a pillow-topped bench and set a sleek chandelier overhead to round out the look.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/mercury-row-marcelo-hand-woven-ivory-area-rug-mcrr7867.html",
        "class_name": "Area Rugs",
        "sale_price": 62.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/57990772/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 90.11,
                "y": 114.14,
                "z": 0.72
            },
            "glb": "http://img.wfrcdn.com/docresources/33808/109/1090615.glb",
            "obj": "http://img.wfrcdn.com/docresources/33808/101/1016867.zip"
        }
    },
    {
        "sku": "MCRW6632",
        "product_name": "Dorset Ivory/Fuchsia Indoor Area Rug",
        "product_description": "Add a pop of pink to any ensemble in your home with this area rug. Blending vintaged charm with a touch of modern flair, it showcases a Persian-inspired motif with a medallion in the center and a matching border. Its vibrant fuchsia and ivory color palette is accented by antiqued detailing, giving this design a balanced and bright look. Machine-woven in Turkey from 100% polypropylene, it is stain- and fade-resistant, making it an ideal anchor for high-traffic spaces. We recommend you pair this piece with a rug pad for extra cushioning and traction underfoot.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/mercury-row-dorset-ivoryfuchsia-indoor-area-rug-mcrw6632.html",
        "class_name": "Area Rugs",
        "sale_price": 24.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/33808/46488007/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 62.98,
                "y": 86.98,
                "z": 0.5
            },
            "glb": "http://img.wfrcdn.com/docresources/44356/107/1077820.glb",
            "obj": "http://img.wfrcdn.com/docresources/44356/94/944092.zip"
        }
    },
    {
        "sku": "MCRW7352",
        "product_name": "Mcguire Ivory/Silver Area Rug",
        "product_description": "Blending a minimalist design with neutral hues, this versatile area rug is right at home in a variety of aesthetics and color palettes. This contemporary anchor showcases a subtle striated pattern in tones that transition from ivory to gray. Power-loomed in Turkey, this piece is stain- and fade-resistant, making it the perfect pick for high-traffic spaces. Featuring a 0.43\" pile height, this base is best paired with a rug pad underneath for extra cushioning and traction.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/mercury-row-mcguire-ivorysilver-area-rug-mcrw7352.html",
        "class_name": "Area Rugs",
        "sale_price": 37.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58133689/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 72,
                "y": 108,
                "z": 0.27
            },
            "glb": "http://img.wfrcdn.com/docresources/33808/107/1072725.glb",
            "obj": "http://img.wfrcdn.com/docresources/33808/76/764667.zip"
        }
    },
    {
        "sku": "MTNA1015",
        "product_name": "Brandt  Machine Woven Indoor Gray Area Rug",
        "product_description": "The table is set, your lights are dimmed down low for ambiance, and you're just putting the finishing touches on each course - this dinner party is about to begin! While eclectic dishes like herb-roasted rack of lamb and stuffed sweet potatoes are sure to delight your guests, your dining room decor might just steal the show! Start by centering your tablescape with a lush overflowing potted plant, then spark conversation between your foodie companions with colorful canvas prints dotting the surrounding walls, and finally anchor it all with this alluring area rug. Made in Turkey, it is machine woven of shed-free polypropylene with a distressed Persian-inspired motif in versatile hues of gray and beige. If your social gatherings are mainly hosted in the living room, just center it in your seating group! It's equally lovely shining solo between a pair of pillow-topped loveseats, or made boldly bohemian with a few plush pouf ottomans scattered around.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/mistana-brandt-machine-woven-indoor-gray-area-rug-mtna1015.html",
        "class_name": "Area Rugs",
        "sale_price": 26.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37055/56364938/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 72,
                "y": 48,
                "z": 0.5
            },
            "glb": "http://img.wfrcdn.com/docresources/37700/107/1072403.glb",
            "obj": "http://img.wfrcdn.com/docresources/37700/76/764251.zip"
        }
    },
    {
        "sku": "MTNA1398",
        "product_name": "Brandt Turquoise Area Rug",
        "product_description": "Pairing an oriental-inspired motif with distressed details, this eye-catching polypropylene rug instantly elevates your favorite aesthetic. Its medallion details add a pop of pattern to your decor, while its turquoise hue blends effortlessly into both monochromatic or vibrant spaces. Lean into this piece's versatility by adding it to a boho chic entryway ensemble alongside a clean-lined console table and tufted storage bench for a complementing look. Dot the table with a trio of antiqued ceramic bird figurines for a whimsical nod to the past, then match it with an array of framed family photos for personal charm. Dot nearby walls with sunburst accents and abstract canvas prints for an eye-catching display, then suspend a geometric pendant above the space to illuminate it in visual appeal.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/mistana-brandt-turquoise-area-rug-mtna1398.html",
        "class_name": "Area Rugs",
        "sale_price": 39.1,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37055/57120511/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 60,
                "y": 96,
                "z": 0.5
            },
            "glb": "http://img.wfrcdn.com/docresources/44356/106/1066102.glb",
            "obj": "http://img.wfrcdn.com/docresources/44356/86/865335.zip"
        }
    },
    {
        "sku": "MTNA1678",
        "product_name": "Clair Dark Gray Area Rug",
        "product_description": "Anchor any arrangement with a dash of global inspiration with this area rug, offering a distressed geometric motif in gray hues to set a stylish foundation for your eclectic ensemble. Power-loomed in Turkey from polypropylene – a durable synthetic material that resists staining and fading – this piece is an ideal anchor for high-traffic rooms in your home. Though this design's medium 0.5\" provides a bit of cushioning underfoot, we recommend you pair it with a rug pad for additional padding and traction.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/mistana-clair-dark-gray-area-rug-mtna1678.html",
        "class_name": "Area Rugs",
        "sale_price": 28.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58137097/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 60,
                "y": 89,
                "z": 0.25
            },
            "glb": "http://img.wfrcdn.com/docresources/37700/107/1072206.glb",
            "obj": "http://img.wfrcdn.com/docresources/37700/76/763999.zip"
        }
    },
    {
        "sku": "MTNA1789",
        "product_name": "Darchelle Beige/Pink Area Rug",
        "product_description": "Ready to stand up to high foot traffic in the entryway and take on occasional spills under the kitchen table, polypropylene rugs are ideal anchors for any mess-prone area of your abode. Take this one for example: made in Turkey, it is power-loomed from that must-have material and features an eye-catching Persian-inspired motif in hues of beige and pink. To keep this piece safely in place, we recommend using a rug pad.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/mistana-darchelle-beigepink-area-rug-mtna1789.html",
        "class_name": "Area Rugs",
        "sale_price": 51.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/46921865/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 48,
                "y": 72,
                "z": 0.25
            },
            "glb": "http://img.wfrcdn.com/docresources/37700/107/1073034.glb",
            "obj": "http://img.wfrcdn.com/docresources/37700/76/764922.zip"
        }
    },
    {
        "sku": "MTNA1822",
        "product_name": "Brandt Dark Grey Area Rug",
        "product_description": "A fine foyer starts with the foundation! Set the tone for your alluring entryway by rolling out this ravishing area rug by the front door, effortlessly grabbing glances as you're greeting guests. Play up its bohemian beauty with a weathered wood console table for staging lush overflowing plants, then lend a little extra light with a gleaming golden pendant hanging overhead. Made in Turkey, this distinctive design is machine woven of polypropylene with latex backing for a casual piece that stays put. Detailed with a distressed Persian-inspired motif that's sure to draw the eye, it's able to beautifully blend into any abode thanks to hues of dark gray and white. Looking to liven up the living room? Just let this posh piece lay down between a pair of pillow-topped loveseats for a cozy seating ensemble, lovely dotted with a smattering of plush pouf ottomans for a dash of boho-chic beauty.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/mistana-brandt-dark-grey-area-rug-mtna1822.html",
        "class_name": "Area Rugs",
        "sale_price": 33.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/44356/43847352/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 48,
                "y": 72,
                "z": 0.3
            },
            "glb": "http://img.wfrcdn.com/docresources/37700/107/1076305.glb",
            "obj": "http://img.wfrcdn.com/docresources/37700/76/764161.zip"
        }
    },
    {
        "sku": "WDLN3892",
        "product_name": "Cangelosi Gray Area Rug",
        "product_description": "A bold, contemporary pinwheel pattern defines this alluring area rug, showcasing soft hues of gray, ivory, and brown. Made in China, this rug is machine woven from a stain and fade-resistant polyester and acrylic blend in a high-low 0.5’’ pile—perfect for laying out in the living room or digging your toes in right out of bed in the morning. Available in a selection of sizes to best suit your space, this rug works best when paired with a rug pad to prevent shifting and sliding.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/wade-logan-cangelosi-gray-area-rug-wdln3892.html",
        "class_name": "Area Rugs",
        "sale_price": 35.98,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36989/26204414/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 91.77,
                "y": 91.63,
                "z": 0.5
            },
            "glb": "http://img.wfrcdn.com/docresources/36989/107/1073047.glb",
            "obj": "http://img.wfrcdn.com/docresources/36989/76/764943.zip"
        }
    },
    {
        "sku": "WLAO3915",
        "product_name": "Aliyah Pink Area Rug",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/willa-arlo-interiors-aliyah-pink-area-rug-wlao3915.html",
        "class_name": "Area Rugs",
        "sale_price": 29.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58129065/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 63,
                "y": 91,
                "z": 0.25
            },
            "glb": "http://img.wfrcdn.com/docresources/37700/107/1072415.glb",
            "obj": "http://img.wfrcdn.com/docresources/37700/76/764263.zip"
        }
    },
    {
        "sku": "WNST3848",
        "product_name": "Kimbell Donohoe Beige/Green Indoor/Outdoor Area Rug",
        "product_description": "This sunny and sensational collection of flat woven indoor/outdoor rugs is pretty, practical and simply perfect for high traffic areas. With its inviting assortment of classic and contemporary designs, tempting color palettes and terrific textures, these multipurpose rugs will afford an air of simple sophistication to any environment.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/winston-porter-kimbell-donohoe-beigegreen-indooroutdoor-area-rug-wnst3848.html",
        "class_name": "Area Rugs",
        "sale_price": 41.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/57101151/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 63.15,
                "y": 89,
                "z": 0.36
            },
            "glb": "http://img.wfrcdn.com/docresources/0/139/1392932.glb",
            "obj": "http://img.wfrcdn.com/docresources/0/141/1413337.zip"
        }
    },
    {
        "sku": "ZPCD5905",
        "product_name": "Kistler Hand-Braided Multi Area Rug",
        "product_description": "An effortless glance-grabber in any space, this alluring area rug is sure to enliven your abode. Roll it out between a pair of crisp white loveseats for a pop of contrast in the living room, then make it shine with flickering candle lanterns atop weathered wood nightstands around the ensemble. Made in India, this ravishing rug is sure to stand out in any space. It is handcrafted of 100% cotton for a soft touch, while a braided design and a rainbow of vibrant hues make it effortlessly eye-catching. Switching up your style in the master suite? Take a solid-hued sumptuous comforter from simple to stunning in seconds by complementing it with this ravishing rug on the floor below. Though this posh piece brims with bohemian beauty all on its own, you can lend a little extra breezy appeal by dotting the walls around with a collection of curated antique prints.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/zipcode-design-kistler-hand-braided-multi-area-rug-zpcd5905.html",
        "class_name": "Area Rugs",
        "sale_price": 28.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30593/55591222/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 36,
                "y": 60,
                "z": 0.5
            },
            "glb": "http://img.wfrcdn.com/docresources/37700/107/1071976.glb",
            "obj": "http://img.wfrcdn.com/docresources/37700/76/763780.zip"
        }
    },
    {
        "sku": "ZPCD6981",
        "product_name": "Gehl Modern Blue Arcs & Shapes Area Rug",
        "product_description": "Outfit your favorite aesthetic in versatile style with this eye-catching rug, an artful addition to any space. Its abstract geometric motif adds a pop of pattern to your decor while its muted hues blend effortlessly into both monochromatic and vibrant spaces. Lean into this piece's transitional influence by adding it to a contemporary living room alongside a streamlined sofa and tufted arm chair for a cohesive ensemble. Dot nearby walls with a rectangle mirror and landscape canvas print for an understated display, then pair it with metal typographic decor for a dash of dimension. Anchor the space with a glass-top coffee table, then use it to display charming flea market finds or a bowl of faux fruit for natural appeal. Equally at home defining high-traffic areas in the entryway, this charming rug instantly elevates your well-appointed decor ensemble.",
        "product_page_url": "https://www.wayfair.com/rugs/pdp/zipcode-design-gehl-modern-blue-arcs-shapes-area-rug-zpcd6981.html",
        "class_name": "Area Rugs",
        "sale_price": 30.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58397785/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 26.99,
                "y": 46.99,
                "z": 0.4
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/107/1073238.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/76/765127.zip"
        }
    },
    {
        "sku": "BCHH7421",
        "product_name": "Stoneford Etagere Bookcase",
        "product_description": "A traditional silhouette gets a contemporary update in this etagere bookcase. Crafted of solid and manufactured wood in a classic painted finish, this bookcase features tasteful moldings, a slatted backing, and X-shaped panel sides. Each clean-lined shelf provides a perfect platform for displaying everything from rows of your favorite reads to framed photos and collected curios. Shipped flat-packed, this bookcase requires full assembly, and should take a team of two about 60 minutes to complete.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/beachcrest-home-stoneford-etagere-bookcase-bchh7421.html",
        "class_name": "Bookcases",
        "sale_price": 75.19,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2445/41669691/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 31.5,
                "y": 11.75,
                "z": 32.5
            },
            "glb": "http://img.wfrcdn.com/docresources/38454/94/942614.glb",
            "obj": "http://img.wfrcdn.com/docresources/38454/101/1019705.zip"
        }
    },
    {
        "sku": "CLOP1021",
        "product_name": "Cubicals Cube Unit Bookcase",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/closetmaid-cubicals-cube-unit-bookcase-clop1021.html",
        "class_name": "Bookcases",
        "sale_price": 94.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36069/16377394/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 47.5,
                "y": 11.6,
                "z": 35.9
            },
            "glb": "http://img.wfrcdn.com/docresources/36069/107/1071333.glb",
            "obj": "http://img.wfrcdn.com/docresources/36069/76/763066.zip"
        }
    },
    {
        "sku": "LRFY1920",
        "product_name": "Ermont Etagere Bookcase",
        "product_description": "Blending the charm of farmhouse aesthetics with modern minimalism, this understated bookcase brings on-trend style to any space in your home. Its compact 56.75\" H x 23.46\" W x 11.62\" D silhouette makes it an ideal option for smaller spaces, while its clean lines and open design ensure it won't overwhelm an existing arrangement. Crafted with a black-finished metal frame, this budget-friendly piece features five tiers made from manufactured wood in a natural finish, each with a weight capacity of 30 lbs., that are perfect for housing linens, cookbooks, or a decorative display. Assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/ermont-etagere-bookcase-lrfy1920.html",
        "class_name": "Bookcases",
        "sale_price": 83.22,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/42526/41294446/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 23.46,
                "y": 11.62,
                "z": 56.77
            },
            "glb": "http://img.wfrcdn.com/docresources/42526/107/1072122.glb",
            "obj": "http://img.wfrcdn.com/docresources/42526/76/763897.zip"
        }
    },
    {
        "sku": "MCRF5348",
        "product_name": "Selzer Geometric Etagere Bookcase",
        "product_description": "More than just a platform to perch your collection of novels, accent pieces, and more, this bookcase offers a touch of glam style to your abode. Constructed from metal, it features a clean-lined frame awash in a warm brass finish, and strikes a rectangular silhouette. Since not all decorative displays come in the same size, it showcases six shelves at different heights and widths to accommodate tall potted plants and eye-catching decorative bowls alike.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercer41-selzer-geometric-etagere-bookcase-mcrf5348.html",
        "class_name": "Bookcases",
        "sale_price": 227.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/60455095/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 40.04,
                "y": 13.01,
                "z": 72.03
            },
            "glb": "http://img.wfrcdn.com/docresources/39355/119/1191264.glb",
            "obj": "http://img.wfrcdn.com/docresources/39355/121/1210988.zip"
        }
    },
    {
        "sku": "MCRR3404",
        "product_name": "Chrysanthos Etagere Bookcase",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercury-row-chrysanthos-etagere-bookcase-mcrr3404.html",
        "class_name": "Bookcases",
        "sale_price": 203.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/33808/43181625/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 34.9,
                "y": 11.96,
                "z": 70.79
            },
            "glb": "http://img.wfrcdn.com/docresources/33808/109/1097492.glb",
            "obj": "http://img.wfrcdn.com/docresources/33808/75/755655.zip"
        }
    },
    {
        "sku": "SEHO2183",
        "product_name": "Bowerbank Cube Unit Bookcase",
        "product_description": "What good is a collection if it’s not properly displayed? Show off your favorite novels, movies, and more with this understated and stylish bookcase featuring ten open compartments (eight small and two large). It’s made from manufactured wood and measures 47.5'' H x 53.13'' W x 12.13'' D while striking a square silhouette, and comes in a solid neutral color for a look that complements any traditional aesthetic. Proudly made in the USA.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/beachcrest-home-bowerbank-cube-unit-bookcase-seho2183.html",
        "class_name": "Bookcases",
        "sale_price": 215.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/59085279/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 52.78,
                "y": 13.02,
                "z": 47.12
            },
            "glb": "http://img.wfrcdn.com/docresources/37308/106/1068437.glb",
            "obj": "http://img.wfrcdn.com/docresources/37308/75/758937.zip"
        }
    },
    {
        "sku": "SEHO9871",
        "product_name": "Oridatown Standard Bookcase",
        "product_description": "Expand your personal library and display your favorite reads, decorative accents, and potted plants with this bookcase. Featuring five shelves – three of which are adjustable – this manufactured wood piece boasts cottage-style details and tapered legs for a look that’s traditionally charming, while x-shaped details on the side round out the look. Wall attachment hardware is included, so you don’t need to worry about it tipping over. Measures 31'' H x 26.61'' W.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/beachcrest-home-oridatown-standard-bookcase-seho9871.html",
        "class_name": "Bookcases",
        "sale_price": 216.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/51576463/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 31.73,
                "y": 12.72,
                "z": 65.98
            },
            "glb": "http://img.wfrcdn.com/docresources/150/110/1104004.glb",
            "obj": "http://img.wfrcdn.com/docresources/150/112/1122853.zip"
        }
    },
    {
        "sku": "ZPCD1459",
        "product_name": "Ricardo Ladder Bookcase",
        "product_description": "Whether you love showing off framed family photos or you want a spot to store your collection of DVDs, this versatile leaning bookcase brings understated appeal and fantastic function to your home. Crafted with manufactured wood, this solid-hued design blends seamlessly into any existing ensemble while offering ample storage space. Place this five-tiered piece in your study to display your favorite books with pride, or tuck it into an unused corner of your living room to use it as a simplistic stage for potted succulents, contemporary sculptures, and sleek vases that will grab glances from guests at your next casual cocktail party.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-ricardo-ladder-bookcase-zpcd1459.html",
        "class_name": "Bookcases",
        "sale_price": 64.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/30593/39337707/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 22,
                "y": 14.5,
                "z": 70
            },
            "glb": "http://img.wfrcdn.com/docresources/37572/107/1071397.glb",
            "obj": "http://img.wfrcdn.com/docresources/37572/76/763118.zip"
        }
    },
    {
        "sku": "ZPCD6675",
        "product_name": "Rutherford Ladder Bookcase",
        "product_description": "Equally ideal for staging and storage space, this beautiful bookcase is a must-have for your abode. Keep it centered against a blank wall in the entryway to put framed family photos on display atop its five open shelves, then add in woven wicker bins to keep out-the-door accessories on hand. Or, if you're working with a smaller space, simply pull it up beside your bed for a nightstand alternative with space to keep a small lamp and stow away morning prep essentials. Taking on a stylish leaning silhouette, this distinctive design is crafted of laminate wood with a gently weathered gray finish.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-rutherford-ladder-bookcase-zpcd6675.html",
        "class_name": "Bookcases",
        "sale_price": 145.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/47459214/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 25.15,
                "y": 18.17,
                "z": 60
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/107/1077406.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/93/935964.zip"
        }
    },
    {
        "sku": "BCHH7429",
        "product_name": "Stoneford Traditional Coffee Table",
        "product_description": "A breezy way to anchor your living room look, this coffee table brings both storage and style to your carefully curated ensemble. Its clean lines are emblematic of traditional styles, and x-shaped sides lend coastal flair. Made from manufactured wood, this design features a lower open shelf perfect for lining with woven wicker bins, while ample space up top makes room for coasters, fanning out magazines, and setting TV remotes.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/beachcrest-home-stoneford-traditional-coffee-table-bchh7429.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 224.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/38454/32250186/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 35.5,
                "y": 35.5,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/38454/109/1092868.glb",
            "obj": "http://img.wfrcdn.com/docresources/38454/76/766575.zip"
        }
    },
    {
        "sku": "DBHC6310",
        "product_name": "Mathis Coffee Table Trunk with Lift Top",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/darby-home-co-mathis-coffee-table-trunk-with-lift-top-dbhc6310.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 349.87,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36984/41918630/1/Woolwich%2BTrunk%2BCoffee%2BTable%2Bwith%2BLift-Top.jpg",
        "model": {
            "dimensions_inches": {
                "x": 46,
                "y": 26,
                "z": 20
            },
            "glb": "http://img.wfrcdn.com/docresources/36984/109/1097498.glb",
            "obj": "http://img.wfrcdn.com/docresources/36984/76/763358.zip"
        }
    },
    {
        "sku": "IVBX2371",
        "product_name": "Sydnor Coffee Table",
        "product_description": "Center your seating space in contemporary style with this clean-lined coffee table. Crafted of metal, this piece features a sizable square top and lower shelf (which both measure 32\" across) that provide a place for snacks, framed photos, a stack of magazines, and more. Clear tempered glass tiers contribute to its open and airy look, while the neutral finish on its frame allows this versatile design to blend with a variety of color palettes and aesthetics. Assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/ivy-bronx-sydnor-coffee-table-ivbx2371.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 122.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/1261/38956912/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 32.01,
                "y": 31.99,
                "z": 17.98
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/107/1077850.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/94/944255.zip"
        }
    },
    {
        "sku": "IVYB7137",
        "product_name": "Evadne Coffee Table",
        "product_description": "A practical piece for any living room, this coffee tables offer a platform for seasonal decor and brings contemporary appeal to your home. Crafted from metal with a brushed nickel finish, the stylish frame features four angled legs connected to a square base. Set to the frame by suction cup hooks, its clear glass tabletop features beveled edges and measures 34.13'' W x 34.13'' D, leaving plenty of real estate available in your living room ensemble. Assembly is required, but no tools are needed.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/ivy-bronx-evadne-coffee-table-ivyb7137.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 180.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2668/51727997/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 34.32,
                "y": 34.18,
                "z": 16.38
            },
            "glb": "http://img.wfrcdn.com/docresources/33808/110/1101629.glb",
            "obj": "http://img.wfrcdn.com/docresources/33808/111/1119781.zip"
        }
    },
    {
        "sku": "LFMF1697",
        "product_name": "Kaitlin Coffee Table",
        "product_description": "Feeling boxed out by square furniture? If you're looking for a way to break up a room with an abundance of blocky pieces, adding a circular accent like this coffee table can be a great selection. Constructed of solid poplar with poplar veneers, this piece features a distressed finish for a country touch in any room. The surface and shelf feature a slat-inspired surface, perfect for a home looking for a rustic accent. Measuring 18'' H x 40'' in diameter, this piece also includes wheels for easy movement.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/kaitlin-coffee-table-lfmf1697.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 377.12,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/1436/60832553/1/Bellagio%2BRound%2BCoffee%2BTable.jpg",
        "model": {
            "dimensions_inches": {
                "x": 40,
                "y": 39.83,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/37306/130/1302505.glb",
            "obj": "http://img.wfrcdn.com/docresources/37306/131/1310103.zip"
        }
    },
    {
        "sku": "LFMF1830",
        "product_name": "Silvis Coffee Table",
        "product_description": "Center your living room or den around charming style with this lovely coffee table. The perfect pick for modern farmhouse aesthetics, it showcases a streamlined frame with a rustic wood top supported by two x-crossed sides. The sides are crafted from metal and finished in a black hue for a touch of industrial appeal, while the lower shelf provides a convenient space to tuck away glossy magazines, media accessories, and more.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/silvis-coffee-table-lfmf1830.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 220.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/29633/41687288/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 47.25,
                "y": 23.75,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/42526/108/1082327.glb",
            "obj": "http://img.wfrcdn.com/docresources/42526/104/1043151.zip"
        }
    },
    {
        "sku": "LGLY2659",
        "product_name": "Finnur Coffee Table",
        "product_description": "This minimalist coffee table's slighly dipped surface and classic walnut finish make it the perfect piece to let your favorite accents take center stage. Add a stack of design books and chic statuette for an artful look, or top it with a vintage vase to play up its midcentury side.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-finnur-coffee-table-lgly2659.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 209.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36991/58163521/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 34.25,
                "y": 34.25,
                "z": 15.75
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/128/1283658.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/129/1290018.zip"
        }
    },
    {
        "sku": "LRFY7375",
        "product_name": "Forteau Coffee Table",
        "product_description": "When movie marathons and cocktail parties come around, you’ll be happy to have this clean-lined coffee table at your side. Crafted with a black-finished metal frame, this budget-friendly piece features two tiers made from manufactured wood in a natural finish for a neutral and understated look. Measuring 18.5'' H x 42'' W x 18.1'' D overall, this design provides essential space to set down snacks, magazines, and more. Assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/forteau-coffee-table-lrfy7375.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 127.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/42526/43997462/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 42,
                "y": 18.1,
                "z": 18.5
            },
            "glb": "http://img.wfrcdn.com/docresources/42526/106/1067866.glb",
            "obj": "http://img.wfrcdn.com/docresources/42526/89/897329.zip"
        }
    },
    {
        "sku": "MCRW5847",
        "product_name": "Treece Coffee Table",
        "product_description": "Inspired by a stylish ski resort in the Italian alps, this cosmopolitan coffee table lends Euro modern appeal to any seating ensemble. Crafted of manufactured wood with veneers in a rich, light gray woodgrain finish, the 2\" thick tabletop strikes an expansive, circular silhouette measuring 35.4\" in diameter. Three iron hairpin legs in a rustic black finish provide sturdy support, elevating the tabletop 12.6\" H to round out the design.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercury-row-treece-coffee-table-mcrw5847.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 191.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36991/34821552/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 35.4,
                "y": 35.4,
                "z": 12.6
            },
            "glb": "http://img.wfrcdn.com/docresources/33808/110/1103949.glb",
            "obj": "http://img.wfrcdn.com/docresources/33808/113/1130196.zip"
        }
    },
    {
        "sku": "MTNA5083",
        "product_name": "Wasser Coffee Table",
        "product_description": "Form meets function when it comes to this clean-lined coffee table, the perfect pick for contemporary and mid-century modern arrangements. Founded atop an open metal base, this piece features a manufactured wood tabletop with a neutral laminate finish that provides a place to put a stack of magazines, a spread of snacks, and beyond. A golden finish on the frame rounds out the look with a hint of glamour. Full assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mistana-wasser-coffee-table-mtna5083.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 126.15,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2381/41123789/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 36.24,
                "y": 36.24,
                "z": 19.11
            },
            "glb": "http://img.wfrcdn.com/docresources/44311/108/1080459.glb",
            "obj": "http://img.wfrcdn.com/docresources/44311/98/983859.zip"
        }
    },
    {
        "sku": "ORNE1883",
        "product_name": "Casas Coffee Table",
        "product_description": "Effortlessly center your living room or den seating group with this timeless coffee table, the perfect pick for classic and contemporary aesthetics alike. Featuring an iron frame with two tempered glass shelves, this low-key coffee table brings a sleek touch to any aesthetic. Use it to keep remotes and other entertainment accessories organized, then clear everything away to make room for trays of cocktails and hors d'oeuvres when party guests arrive.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/orren-ellis-casas-coffee-table-orne1883.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 164.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/1261/40681275/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 36.05,
                "y": 36.05,
                "z": 18.01
            },
            "glb": "http://img.wfrcdn.com/docresources/44325/109/1097058.glb",
            "obj": "http://img.wfrcdn.com/docresources/44325/105/1050775.zip"
        }
    },
    {
        "sku": "ORNE9301",
        "product_name": "Seguin Coffee Table",
        "product_description": "Both luxurious and simple, the Seguin Coffee Table offers a touch of elegance with functionality. Made of a durable, painted metal base with a smooth finish and a polished faux marble top, this piece can take your home decor to the next level in charm.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/orren-ellis-seguin-coffee-table-orne9301.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 112.61,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/57678532/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 42,
                "y": 22,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/44325/126/1268624.glb",
            "obj": "http://img.wfrcdn.com/docresources/44325/127/1277969.zip"
        }
    },
    {
        "sku": "RDBT4847",
        "product_name": "Drayton Lift Top Coffee Table",
        "product_description": "Add some unique style and functionality to your home with this lift-top coffee table from this collection. The top lifts up and forward creating a multi purpose work surface so you can browse online or eat dinner while relaxing on your couch. Other features include hidden storage beneath the top and open shelves for storing blankets, board games or knick-knacks. This versatile coffee table will give your home a fresh new look.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/red-barrel-studio-drayton-lift-top-coffee-table-rdbt4847.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 195.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/34591/55521045/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 43,
                "y": 19.5,
                "z": 18.69
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/110/1107980.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/113/1137682.zip"
        }
    },
    {
        "sku": "THPS2723",
        "product_name": "Brassiewood Coffee Table",
        "product_description": "With its clean-cut looks and timeless style, this charming coffee table is an excellent addition to any living room seating ensemble. Crafted from solid pine and manufactured wood, this contemporary design strikes a 44” x 22” rectangular silhouette in an antique tobacco brown finish with A-brace accents and four square legs. A wide lower shelf offers a perfect platform for displaying a stack of your favorite books or fanning out your preferred periodicals, while the expansive tabletop offers plenty of space for remotes, coasters, and other couchside essentials.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-brassiewood-coffee-table-thps2723.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 146.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30973/43998656/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 44,
                "y": 22,
                "z": 19.99
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/106/1066816.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/86/869729.zip"
        }
    },
    {
        "sku": "THPS4100",
        "product_name": "Aldridge Terrarium Coffee Table",
        "product_description": "Show off your unique style with this exciting display coffee table. The terrarium-style design is ideal for creating indoor gardens or showcasing your fondest memories and keepsakes. Glass panels are set within black framing with silver distressing for a refreshing look that complements many styles and décor. This captivating table brings the outdoors in and is ideal for lowlight houseplants or succulents. Slight variations in distressed finish may occur.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-aldridge-terrarium-coffee-table-thps4100.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 186.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/1261/59870376/1/Terrarium%2BCoffee%2BTable.jpg",
        "model": {
            "dimensions_inches": {
                "x": 42.67,
                "y": 20.86,
                "z": 18.57
            },
            "glb": "http://img.wfrcdn.com/docresources/0/140/1406914.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/121/1217488.zip"
        }
    },
    {
        "sku": "TRNT2115",
        "product_name": "Anissa Coffee Table with Storage",
        "product_description": "Industrial and on-trend, this clean-lined console table brings a touch of understated style to your living room ensemble. Measuring 47.25\" W 23.75\" D, the manufactured wood tabletop strikes a bowed rectangular silhouette in a rustic speckled gray finish, while its powder-coated metal frame features open sides for an airy appearance. Between the tabletop and a matching lower shelf, there’s plenty of room to display coasters and remotes, magazines, and more!",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/trent-austin-design-anissa-coffee-table-with-storage-trnt2115.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 124.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36987/42008362/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 47.25,
                "y": 23.98,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/37312/107/1073231.glb",
            "obj": "http://img.wfrcdn.com/docresources/37312/76/765118.zip"
        }
    },
    {
        "sku": "WADL4054",
        "product_name": "Luther Coffee Table",
        "product_description": "Featuring a bold, open design and white lacquer finish, this eye-catching table is the perfect anchor for any ensemble. Set it over a lush shag rug to up its midcentury modern appeal, and then use its 3 tiers to display stacked art books, faux fruit, and more.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/wade-logan-luther-coffee-table-wadl4054.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 259.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36989/27049671/1/Breean%2BCoffee%2BTable.jpg",
        "model": {
            "dimensions_inches": {
                "x": 46.91,
                "y": 23.5,
                "z": 15.97
            },
            "glb": "http://img.wfrcdn.com/docresources/36989/108/1088792.glb",
            "obj": "http://img.wfrcdn.com/docresources/36989/100/1001971.zip"
        }
    },
    {
        "sku": "WLFR1664",
        "product_name": "Arianna Coffee Table",
        "product_description": "Characterized by its clean lines and open design, this understated coffee table brings a touch of modern minimalism to your living room layout.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/williston-forge-arianna-coffee-table-wlfr1664.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 106.43,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2381/43690603/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 42,
                "y": 24,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/44321/107/1079604.glb",
            "obj": "http://img.wfrcdn.com/docresources/44321/97/979407.zip"
        }
    },
    {
        "sku": "WRLO2038",
        "product_name": "Jerlene Glam Coffee Table",
        "product_description": "Sprinkle a touch of glamour into your living room layout with this chic coffee table. Crafted from manufactured wood, this rectangular design is finished in matte silver and lined with mirrored panels to reflect lots of light throughout your space.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/willa-arlo-interiors-jerlene-glam-coffee-table-wrlo2038.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 259.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37313/46836970/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 42,
                "y": 23,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/44357/107/1077944.glb",
            "obj": "http://img.wfrcdn.com/docresources/44357/94/945999.zip"
        }
    },
    {
        "sku": "ZPCD1733",
        "product_name": "Wylie Rectangular 1 Drawer Coffee Table",
        "product_description": "Center your well-appointed living room or den seating group in simple style with this essential coffee table, the perfect balance of clean-lined, loft-worthy looks and effortless utility in your ensemble. Defined by a simple manufactured wood design with classic woodgrain details, this piece offers a neutral touch to your look, while its open side shelves, wide drawers, and metal bar pull add a dash of definition and contemporary appeal to the space. Top it off with a spread of glossy fashion magazines for an upscale twist in the room, then arrange the open shelves with potted succulents or glossy ceramic vases to round out the environment.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-wylie-rectangular-1-drawer-coffee-table-zpcd1733.html",
        "class_name": "Coffee & Cocktail Tables",
        "sale_price": 167.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36987/41460060/1/Coalmont%2BCoffee%2BTable.jpg",
        "model": {
            "dimensions_inches": {
                "x": 47.1,
                "y": 24.46,
                "z": 16
            },
            "glb": "http://img.wfrcdn.com/docresources/36987/109/1095226.glb",
            "obj": "http://img.wfrcdn.com/docresources/36987/76/768424.zip"
        }
    },
    {
        "sku": "ALTH6694",
        "product_name": "Weare Solid Back Skirted Upholstered Dining Chair",
        "product_description": "Equally suited to deck out the dining room or spruce up an unused corner of the master suite, this versatile dining chair brings a touch of traditional style to any space. Proudly crafted in the USA, this piece is made with a wood frame, foam fill, sinuous spring supports, and polyester-cotton fabric upholstery. Though its solid hue may seem understated at first, this design showcases a pleated skirt and a rolled back for plenty of classic character.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/alcott-hill-weare-solid-back-skirted-upholstered-dining-chair-alth6694.html",
        "class_name": "Dining Chairs",
        "sale_price": 215.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/40128/43554375/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 20.48,
                "y": 26.48,
                "z": 38.65
            },
            "glb": "http://img.wfrcdn.com/docresources/36985/130/1308929.glb",
            "obj": "http://img.wfrcdn.com/docresources/36985/131/1311929.zip"
        }
    },
    {
        "sku": "BCHH7332",
        "product_name": "Royal Palm Beach Solid Wood Dining Chair",
        "product_description": "Whether you're bringing a breezy touch to your eat-in kitchen or rounding out the dining room in traditional style, this pair of dining chairs is sure to tie your look together. Crafted from solid rubberwood, this chair offers an eco-friendly touch to your ensemble, while its openwork slat design and slanted back brings a timeless, nautical twist to the piece. Best of all, the upkeep is easy—simply wipe it clean with a dry cloth when you're tidying up the room.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/beachcrest-home-royal-palm-beach-solid-wood-dining-chair-bchh7332.html",
        "class_name": "Dining Chairs",
        "sale_price": 108.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/38454/40689222/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 21.5,
                "y": 20.76,
                "z": 36.48
            },
            "glb": "http://img.wfrcdn.com/docresources/38454/127/1273589.glb",
            "obj": "http://img.wfrcdn.com/docresources/38454/127/1279717.zip"
        }
    },
    {
        "sku": "BL18281",
        "product_name": "Sowerby Solid Wood Dining Chair",
        "product_description": "Between dinner parties, festive family feasts, and casual meals alike – your dining room is often entertaining! Spruce up your ensemble for all sorts of events with this stylish side chair. Traditional with its angled legs and rounded spindle back, this solid rubberwood design is still versatile with a neutral solid finish. Measures 35.5'' H x 17.75'' W x 20.75'' D. Assembly for this product is required. Arrives in a set of two.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/birch-lane-sowerby-solid-wood-dining-chair-bl18281.html",
        "class_name": "Dining Chairs",
        "sale_price": 137.95,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/25006/34139319/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 17.88,
                "y": 20.72,
                "z": 35.44
            },
            "glb": "http://img.wfrcdn.com/docresources/25006/131/1315151.glb",
            "obj": "http://img.wfrcdn.com/docresources/25006/131/1319093.zip"
        }
    },
    {
        "sku": "LGLY2171",
        "product_name": "Whiteabbey Side Chair",
        "product_description": "Inspired by iconic mid-century modern design, this marvelous molded arm chair makes an artful addition to any seating ensemble. Its molded plastic seat features a sculpted, swooping back, gently turned arms, and a contoured seat. Four round, tapered, solid wood legs flare out for an architectural appearance, while metal cross braces offer extra support. Since this piece is made from plastic, it's water-resistant, making it a great choice for the kitchen table!",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-whiteabbey-side-chair-lgly2171.html",
        "class_name": "Dining Chairs",
        "sale_price": 75.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36991/23882070/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 24.5,
                "y": 22.14,
                "z": 31.9
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/106/1068465.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/75/755681.zip"
        }
    },
    {
        "sku": "LGLY5216",
        "product_name": "Harrison Dining Chair",
        "product_description": "Inspired by mid-century designs, this lovely chair brings contemporary style and inviting appeal to your ensemble. Perfect in your dining room or pulled up to your desk, is showcases a chic retro frame with a rounded seats and flared legs. The seat is crafted from polypropylene, which is contoured to fit the body, and it is available in multiple solid, crisp finishes, so you can find the right hue for your home. The beech wood legs are connected with black crisscross accenting.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-harrison-dining-chair-lgly5216.html",
        "class_name": "Dining Chairs",
        "sale_price": 75.35,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/49117165/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 18.48,
                "y": 20.25,
                "z": 31.75
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/108/1083341.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/104/1047964.zip"
        }
    },
    {
        "sku": "LGLY6534",
        "product_name": "Quintus Dining Chair",
        "product_description": "You're going to love the clean, modern look of the Quintus Dining Chair. Perfect for a dining area with a decidedly contemporary aesthetic, this chair easily transitions to the home office or living area. The chair boasts a cool matte plastic seat with gentle curves that ensure comfort. The seat rests atop a base featuring four angled wood legs with X-wires stretched between. Geometrically appealing and minimalist, the Quintus is just what your dining table craves.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-quintus-dining-chair-lgly6534.html",
        "class_name": "Dining Chairs",
        "sale_price": 215.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/38610/46371597/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 18.5,
                "y": 21,
                "z": 32.5
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/116/1161510.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/117/1173440.zip"
        }
    },
    {
        "sku": "LGLY6932",
        "product_name": "Brook Decatur Side Chair",
        "product_description": "Drawing inspiration from mid-century and industrial styles, this streamlined side chair brings a touch of vintage flair to your dining ensemble. Founded atop four slender legs finished in black, this arched seat is enveloped in polyurethane upholstery for a budget-friendly and easy-to-clean alternative to genuine leather. Its neutral hues allow it to blend with the color palette of your existing arrangement, while subtle stitch accenting lends this understated design a dash of distinction. After assembly, it supports up to 250 lbs.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-brook-decatur-side-chair-lgly6932.html",
        "class_name": "Dining Chairs",
        "sale_price": 130.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/46120625/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 18.07,
                "y": 20.72,
                "z": 33.18
            },
            "glb": "http://img.wfrcdn.com/docresources/37312/107/1078574.glb",
            "obj": "http://img.wfrcdn.com/docresources/37312/97/970311.zip"
        }
    },
    {
        "sku": "LOON2803",
        "product_name": "Kaiser Point Side Chair",
        "product_description": "This handsome chair serves up elegance, family style. Inspired by the classic designs found in secluded mountain cabins and lakeside lodges, this charming chair is brimming with rustic appeal. The slatted back design and the simple silhouette gives this piece a touch of traditional style, while the wood frame with grain detailing and neutral-toned upholstery anchor it in cabin-chic style. Try pulling six of these lovely chairs around a matching wood table in your dining room, then roll out a simple gray geometric patterned rug to anchor the ensemble. Tired after a long day on the ski slopes? Or maybe you want to get your strength back after a long mountain hike? Whatever the occasion, this charming ensemble is now the perfect place for a cozy, comforting meal. Set the table with crisp white serveware and burlap placemats, then bring out a pot roast, home-baked bread, roasted veggies, and a growler of local craft beer.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/loon-peak-kaiser-point-side-chair-loon2803.html",
        "class_name": "Dining Chairs",
        "sale_price": 64.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37311/41294315/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 51.08,
                "y": 37.62,
                "z": 38.25
            },
            "glb": "http://img.wfrcdn.com/docresources/37311/106/1068638.glb",
            "obj": "http://img.wfrcdn.com/docresources/37311/75/759014.zip"
        }
    },
    {
        "sku": "LRFY6447",
        "product_name": "Gage Side Chair",
        "product_description": "Evoking elements of rustic, traditional, and farmhouse styles, this versatile wood chair is a handsome addition to any seating group. Its woven rattan upholstery adds breezy style to any space while its wood grain details pair perfectly with reclaimed teak accents and plank-inspired wall decor. Add this chair to the living room to complement a cozy cottage arrangement, then pair it with a cable-knit throw blanket for a casual look. Finally, round out the room with a hand-woven jute rug for a subtle touch of texture. With its open-x back and curved base, this eye-catching design adds sophisticated style to your well-appointed home.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/gage-side-chair-lrfy6447.html",
        "class_name": "Dining Chairs",
        "sale_price": 95.5,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/42526/57676771/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 20.56,
                "y": 19.52,
                "z": 34.43
            },
            "glb": "http://img.wfrcdn.com/docresources/42526/125/1258223.glb",
            "obj": "http://img.wfrcdn.com/docresources/42526/126/1263423.zip"
        }
    },
    {
        "sku": "LRKM1961",
        "product_name": "Gennevilliers Ladder Back Solid Wood Dining Chair",
        "product_description": "Bring cottage-chic style to your space with this classic two-tone dining chair. Crafted of solid rubberwood, this chair features a curved backrest with turned ball finials and a classic ladder back, while its lathed legs incorporate structural support braces into their design. Rounding out the design, the box seat features a removable woven rush cushion. Measuring 38.5\" H x 16.25\" W x 17\" D overall, this chair has an 18\" seat height and a 250 lbs. weight capacity.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/lark-manor-gennevilliers-ladder-back-solid-wood-dining-chair-lrkm1961.html",
        "class_name": "Dining Chairs",
        "sale_price": 141.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37307/32355076/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 16.25,
                "y": 17,
                "z": 38.5
            },
            "glb": "http://img.wfrcdn.com/docresources/37306/107/1071141.glb",
            "obj": "http://img.wfrcdn.com/docresources/37306/76/762893.zip"
        }
    },
    {
        "sku": "MCRW5804",
        "product_name": "Cleland Parsons Chair",
        "product_description": "Perfect pulled up to your kitchen or dining room table, this firm and structured side chair features exposed rubberwood legs and a hue.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercury-row-cleland-parsons-chair-mcrw5804.html",
        "class_name": "Dining Chairs",
        "sale_price": 275.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/40981901/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 19.5,
                "y": 23.99,
                "z": 34.16
            },
            "glb": "http://img.wfrcdn.com/docresources/33808/107/1073023.glb",
            "obj": "http://img.wfrcdn.com/docresources/33808/76/764913.zip"
        }
    },
    {
        "sku": "MCRW7640",
        "product_name": "Krol Side Chair",
        "product_description": "Pull up chic style to your dining ensemble or living room arrangement with this four-piece side chair set. A sleek design with modern inspiration, each piece showcases a streamlined silhouette with four flared legs. The base is crafted from metal, while the carved seat and backrest are crafted from MDF. This stackable chair has an armless design, so you can easily set them around your dining room table or kitchen nook.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercury-row-krol-side-chair-mcrw7640.html",
        "class_name": "Dining Chairs",
        "sale_price": 209.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58872295/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 18.33,
                "y": 19.8,
                "z": 34.41
            },
            "glb": "http://img.wfrcdn.com/docresources/10387/122/1229625.glb",
            "obj": "http://img.wfrcdn.com/docresources/10387/123/1235886.zip"
        }
    },
    {
        "sku": "MITN2716",
        "product_name": "Giana Paisley Parsons Chair",
        "product_description": "A classic design gets an on-trend update with this streamlined Parsons chair. Polyester-blend upholstery envelops the seat, showcasing a traditional paisley pattern in bright coral, turquoise, green, and cream hues to bring a splash of color to your space.  Crafted with a solid wood frame that supports up to 250 lbs., this piece is founded atop four straight legs finished in brown with practical foot pads underneath to protect your floors from scratching.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mistana-giana-paisley-parsons-chair-mitn2716.html",
        "class_name": "Dining Chairs",
        "sale_price": 162.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37700/39068913/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 19.03,
                "y": 23.43,
                "z": 37.97
            },
            "glb": "http://img.wfrcdn.com/docresources/37700/116/1164315.glb",
            "obj": "http://img.wfrcdn.com/docresources/37700/117/1174632.zip"
        }
    },
    {
        "sku": "ORNE7051",
        "product_name": "Nunley Arm Chair",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/orren-ellis-nunley-arm-chair-orne7051.html",
        "class_name": "Dining Chairs",
        "sale_price": 169.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/58699570/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 24.17,
                "y": 23.9,
                "z": 31.77
            },
            "glb": "http://img.wfrcdn.com/docresources/44325/119/1197014.glb",
            "obj": "http://img.wfrcdn.com/docresources/44325/121/1213711.zip"
        }
    },
    {
        "sku": "RDBL3915",
        "product_name": "Gentry Mid-Back Dining Chair with Arms",
        "product_description": "Founded atop base, this chair is ready to roll at any desk or dining ensemble. Its frame is traditional with a retro twist, pairing finishes of cream and medium oak wood on a metal frame. The seat is padded with foam and wrapped in oatmeal-hued microfiber upholstery, offering comfort as you kick back. Measures 38'' H x 22.5'' W x 19'' D.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/red-barrel-studio-gentry-mid-back-dining-chair-with-arms-rdbl3915.html",
        "class_name": "Dining Chairs",
        "sale_price": 207,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/49944302/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 22.5,
                "y": 23.86,
                "z": 38
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/110/1100621.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/110/1109784.zip"
        }
    },
    {
        "sku": "RDBL5487",
        "product_name": "Malcolm Captains Armchair",
        "product_description": "Whether you're looking for a charming chair to complete your entertainment ensemble or you're just starting to curate a stately study, this versatile armchair is an alluring addition to your home. Crafted from solid wood, it features a medium walnut finish and dark-brown, faux leather upholstery that blends seamlessly into any existing arrangement. Tuck it beside matching seats to set the foundation for a tasteful dining room, then anchor the space with a turned-leg table that enhances its traditional appeal. Once you love your layout, put down a pair of shimmery metal candlesticks for a classic centerpiece that complements to this piece's nailhead trim.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/red-barrel-studio-malcolm-captains-armchair-rdbl5487.html",
        "class_name": "Dining Chairs",
        "sale_price": 229.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/47042902/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 25,
                "y": 25.01,
                "z": 31.02
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/107/1077937.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/94/945902.zip"
        }
    },
    {
        "sku": "TADN2219",
        "product_name": "Fortuna Side Chair",
        "product_description": "Lend a touch of loft-worthy flair to your dining space with this elegant side chair. Inspired by the designs found in industrial uptown apartments and converted-factory spaces, this chair will imbue your home with vintaged flair and urban sophistication. The steel frame and wood seat gives this piece a touch of textural contrast, while the distressed finish and rounded open back anchor it with industrial appeal. Try pulling six of these sleek seats around a wood-topped dining table with metal legs in your dining room to set a loft-inspired foundation, then build on your look by rolling out a simple gray rug underfoot and dot your walls with metal art work and antiqued typographic prints.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/trent-austin-design-fortuna-side-chair-tadn2219.html",
        "class_name": "Dining Chairs",
        "sale_price": 128.02,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/42583854/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 37.5,
                "y": 21,
                "z": 32.5
            },
            "glb": "http://img.wfrcdn.com/docresources/37312/109/1095466.glb",
            "obj": "http://img.wfrcdn.com/docresources/37312/76/768762.zip"
        }
    },
    {
        "sku": "THRE9388",
        "product_name": "Dyer Side Chair",
        "product_description": "Outfit your dining room with this elegant side chair, made of classic linen upholstery, with a button-tufted design.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-dyer-side-chair-thre9388.html",
        "class_name": "Dining Chairs",
        "sale_price": 174.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/30973/33464761/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 19.11,
                "y": 24.48,
                "z": 37.7
            },
            "glb": "http://img.wfrcdn.com/docresources/29633/108/1089029.glb",
            "obj": "http://img.wfrcdn.com/docresources/29633/100/1003962.zip"
        }
    },
    {
        "sku": "THRE9535",
        "product_name": "Back Bay Side Chair",
        "product_description": "Add a down-home, rustic twist to any entertainment space or seating group with this essential side chair, a subtle touch for your traditional aesthetic. Let a pair sit in the entryway with a matching pedestal side table to give guests a place to sit and kick off their shoes, then hang up a matching wood coat rack above to keep scarves and hats corralled. Crafted from rubberwood, this design makes a lasting and durable addition to any ensemble. Set four around your kitchen table to enjoy weekend breakfasts and casual dinners for years to come, then play with its openwork back by arranging a simple trellis rug on the hardwood floor below.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-back-bay-side-chair-thre9535.html",
        "class_name": "Dining Chairs",
        "sale_price": 143.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/30973/33770329/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 18.72,
                "y": 22.76,
                "z": 39.34
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/107/1072108.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/76/763881.zip"
        }
    },
    {
        "sku": "CSTU1277",
        "product_name": "Goodyear Mid Century Modern Wood Dining Table",
        "product_description": "The heart of your entertaining ensemble is your dining table. Not only is it the spot where you serve up dinner party courses and festive family feasts, but it sets the aesthetic tone for your room and allows you to stage centerpieces that are all your own. Just take a look at this one for example: Brimming with mid-century style, its solid pine wood frame features splayed legs and a natural finish.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/corrigan-studio-goodyear-mid-century-modern-wood-dining-table-cstu1277.html",
        "class_name": "Dining Tables",
        "sale_price": 169.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/54770290/1/furniture%2Fpdp%2Fcorrigan-studio-goodyear-mid-century-modern-wood-dining-table.jpg",
        "model": {
            "dimensions_inches": {
                "x": 47.19,
                "y": 29.49,
                "z": 29.08
            },
            "glb": "http://img.wfrcdn.com/docresources/36990/112/1125477.glb",
            "obj": "http://img.wfrcdn.com/docresources/36990/114/1143111.zip"
        }
    },
    {
        "sku": "GRNW1016",
        "product_name": "Valerie Dining Table",
        "product_description": "Gather friends and family for Sunday brunch or weeknight meals around this lovely dining table, featuring carved legs.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/grain-wood-furniture-valerie-dining-table-grnw1016.html",
        "class_name": "Dining Tables",
        "sale_price": 413.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36861/17945125/1/Valerie%2B63%2BInch%2BDining%2BTable.jpg",
        "model": {
            "dimensions_inches": {
                "x": 63.02,
                "y": 36,
                "z": 31
            },
            "glb": "http://img.wfrcdn.com/docresources/36861/109/1098783.glb",
            "obj": "http://img.wfrcdn.com/docresources/36861/109/1098784.zip"
        }
    },
    {
        "sku": "LFMF2357",
        "product_name": "Colborne Extendable Dining Table",
        "product_description": "Set a simply stylish and rustic anchor in your dining room with this understated table, featuring an acacia hardwood design and cool, salvaged gray finish. Expecting a few extra guests for dinner tonight? This table features an extendable design that lets you accommodate long guest lists at any occasion. Lay the leaf down to expand your tablescape, then set down crisp white plates and shimmering LED candles to round out your low-key, yet elevated look.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/colborne-extendable-dining-table-lfmf2357.html",
        "class_name": "Dining Tables",
        "sale_price": 844.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37311/55617130/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 39.5,
                "y": 82.98,
                "z": 29.99
            },
            "glb": "http://img.wfrcdn.com/docresources/37311/106/1068542.glb",
            "obj": "http://img.wfrcdn.com/docresources/37311/106/1068545.zip"
        }
    },
    {
        "sku": "LGLY3140",
        "product_name": "Santa Maria Dining Table",
        "product_description": "Host festive family feasts and elegant dinner parties alike with this stylish table, finished in solid walnut and featuring beveled edges. Try topping it with a patterned runner and shining chandelier for an eye-catching dining room look, or simply add glossy white dinnerware and stainless steel silverware to craft a minimalist tablescape.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-santa-maria-dining-table-lgly3140.html",
        "class_name": "Dining Tables",
        "sale_price": 391.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/58289480/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 71.05,
                "y": 35.69,
                "z": 29.81
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/128/1288360.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/129/1293441.zip"
        }
    },
    {
        "sku": "LGLY3779",
        "product_name": "Evangeline Dining Table",
        "product_description": "Whether you're adding a contemporary touch to your updated and loft-worthy aesthetic or leaning into a mid-century modern look in your abode, this eye-catching dining table brings a bit of trendy appeal to your space. Featuring splayed beech wood legs with black steel hardware, this dining table showcases with a dash of earthy and rustic character, while the round top provides the perfect stage for blooming bouquets and low-key place settings.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-evangeline-dining-table-lgly3779.html",
        "class_name": "Dining Tables",
        "sale_price": 161.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/57909462/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 39.5,
                "y": 39.5,
                "z": 29.75
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/126/1265999.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/127/1274344.zip"
        }
    },
    {
        "sku": "LGLY3909",
        "product_name": "Paterson Dining Table",
        "product_description": "Enjoy this stylish wooden dining table in your home. Featuring a beautiful finish, combined with its concave legs, this table is sure to impress. This table will look good, no matter the décor and will allow you to both host and dine with ease.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-paterson-dining-table-lgly3909.html",
        "class_name": "Dining Tables",
        "sale_price": 339.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/56086313/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 59,
                "y": 35.5,
                "z": 29.69
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/112/1127524.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/115/1152268.zip"
        }
    },
    {
        "sku": "LGLY5881",
        "product_name": "Sheryl Dining Table",
        "product_description": "The mid-century Scandinavian design of this oval dining table is not only characteristically simple and functional but exudes an aesthetic beauty as well. The dining table’s 4-legged center frame is expertly crafted from Solid Oak available in natural or a stained rich walnut finish. Its 70.5\" oval veneered wood top reveals an inviting starburst design that evokes a calming effect, further enhancing your dining experience. The dining table-Oval comfortably seats up to 8 guests.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-sheryl-dining-table-lgly5881.html",
        "class_name": "Dining Tables",
        "sale_price": 503.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36990/35198555/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 70.5,
                "y": 43.5,
                "z": 29.5
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/113/1132057.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/115/1155925.zip"
        }
    },
    {
        "sku": "LRFY7401",
        "product_name": "Fortunat Extendable Dining Table",
        "product_description": "Anchor your dining room in modern farmhouse style with this extendable dining table. Crafted of solid hardwood with laminate veneers in a white limed finish, the tabletop strikes a 48\" W x 48\" D circular silhouette with distressed edges for a charming, well-worn look. Rounding out the design, the turned pedestal base includes four molded feet for sturdy support. Perfect for school night dinners and full-on family feasts alike, this table comfortably seats four as-is, or up to six with the addition of the included lift-off leaf.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/fortunat-extendable-dining-table-lrfy7401.html",
        "class_name": "Dining Tables",
        "sale_price": 602.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/61515678/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 65.5,
                "y": 48,
                "z": 30.25
            },
            "glb": "http://img.wfrcdn.com/docresources/36984/108/1089562.glb",
            "obj": "http://img.wfrcdn.com/docresources/36984/100/1009406.zip"
        }
    },
    {
        "sku": "LRKM2887",
        "product_name": "Ewenn Extendable Dining Table",
        "product_description": "Anchor your dining room in French Country style with this wonderfully Ewenn Extendable Dining Table. Made from solid and manufactured hardwoods with solid acacia veneers in a distressed Dark Walnut finish, this charming design showcases a smooth planked tabletop and an intricately-carved reverse scroll trestle base with a metal crossbar. Two removable leaves expand the table to comfortably accommodate up to eight, while tasteful millwork and moldings offer charismatic craftsmanship and traditional charm. Add to the Pastoral panache by rolling out a soft quatrefoil area rug underfoot for a pleasant pop of pattern, then pull four slatted-back side chairs and two upholstered armchairs around this table as an inviting seating option for weeknight family meals and weekend dinner parties with friends alike.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/lark-manor-ewenn-extendable-dining-table-lrkm2887.html",
        "class_name": "Dining Tables",
        "sale_price": 1274.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37307/36605737/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 112,
                "y": 42,
                "z": 30
            },
            "glb": "http://img.wfrcdn.com/docresources/37152/107/1077497.glb",
            "obj": "http://img.wfrcdn.com/docresources/37152/94/942084.zip"
        }
    },
    {
        "sku": "MCRW5608",
        "product_name": "Carrion Dining Table",
        "product_description": "Brimming with visual appeal, this handsome poplar wood dining table instantly elevates your stylish abode. Its striking pedestal base brings wow-worthy style to your decor, while its rich brown palette is perfect set against a crisp white wall for an accentuating look. Lean into this table's transitional influence by adding it to a contemporary dining room alongside an array of streamlined leather side chairs for a cohesive arrangement, then suspend a geometric pendant above the room to illuminate it in eye-catching style. Dot nearby walls with black-and-white canvas prints and medallion accents for an artful arrangement, then match the display with an oval beveled mirror to open up the space.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercury-row-carrion-dining-table-mcrw5608.html",
        "class_name": "Dining Tables",
        "sale_price": 460.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/55619311/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 50,
                "y": 50,
                "z": 30
            },
            "glb": "http://img.wfrcdn.com/docresources/39354/80/801604.glb",
            "obj": "http://img.wfrcdn.com/docresources/39354/76/761165.zip"
        }
    },
    {
        "sku": "TADN9153",
        "product_name": "Millicent Extendable Dining Table",
        "product_description": "Whether you’re setting up a small dining room or outfitting an open concept den, this compact extendable dining table can be the perfect fit. Made from solid wood with richly distressed oak veneers, this convertible design features a planked rectangular tabletop with rustic metal brackets that let you fold the table up into a console or sofa table, or unfold and expand into a dining table to comfortably seat up to four. Establish an understated industrial aesthetic in your eat-in kitchen by rolling out a cowhide area rug to define the space, then pull four leather upholstered dining chairs up to this charismatic table for an inviting spot to enjoy casual meals with family or after-dinner drinks with friends. For a perfect finishing touch, install a sputnik chandelier overhead to illuminate the scene in a glimmering glow.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/trent-austin-design-millicent-extendable-dining-table-tadn9153.html",
        "class_name": "Dining Tables",
        "sale_price": 339.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/55935868/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 48,
                "y": 18,
                "z": 30
            },
            "glb": "http://img.wfrcdn.com/docresources/37312/106/1066722.glb",
            "obj": "http://img.wfrcdn.com/docresources/37312/86/869058.zip"
        }
    },
    {
        "sku": "THPS1031",
        "product_name": "Fortville Extendable Dining Table",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-fortville-extendable-dining-table-thps1031.html",
        "class_name": "Dining Tables",
        "sale_price": 599.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/30973/35498891/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 59.67,
                "y": 41.97,
                "z": 30.16
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/119/1199922.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/122/1220773.zip"
        }
    },
    {
        "sku": "THPS8641",
        "product_name": "Ellisville Dining Table",
        "product_description": "Traditional charm arrives in your kitchen with this timeless dining table. Founded atop four angled cabriole legs, its base takes on a turned pedestal design. Its frame is constructed from manufactured wood, showcasing a neutral white finish for versatility. Measuring 47.25'' circular, it offers space to seat four for casual morning meals and upscale dinner parties alike. To keep it looking sharp, we recommend wiping clean with a dry cloth. Assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-ellisville-dining-table-thps8641.html",
        "class_name": "Dining Tables",
        "sale_price": 329.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/55631203/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 47.14,
                "y": 47.14,
                "z": 30.38
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/108/1086194.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/108/1086195.zip"
        }
    },
    {
        "sku": "TRPT5301",
        "product_name": "Boothby Round 42\" Dual Drop Leaf Dining Table",
        "product_description": "From sitting down with the morning paper to serving up a home-cooked meal, this drop-leaf dining table is a perfect pick for breakfast nooks, short-on-space dining areas, and the like. It’s built from solid wood and sports a round top, measuring 42'' wide when fully extended and 24'' wide when fully collapsed,  along with a turned pedestal base that brings a hint of traditional influence home. Plus, it seats four comfortably.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-boothby-round-42-dual-drop-leaf-dining-table-trpt5301.html",
        "class_name": "Dining Tables",
        "sale_price": 183.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37306/23719570/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 33,
                "y": 42,
                "z": 29.5
            },
            "glb": "http://img.wfrcdn.com/docresources/37306/109/1098755.glb",
            "obj": "http://img.wfrcdn.com/docresources/37306/109/1098756.zip"
        }
    },
    {
        "sku": "WLAO3771",
        "product_name": "Affric Glass Dining Table",
        "product_description": "Anchor your dining space in glamorous contemporary style with this striking dining table. Crafted of tempered glass, the 3.5\" thick tabletop strikes a 54\" x 54\" circular silhouette with a stylish beveled edge and a protective metal border. Sporting a gleaming polished chrome finish, the hexagonal trestle base made from nickel-plated metal features quatrefoil-inspired side paneling to round out the design. Perfect for intimate dinners and family feasts alike, this table comfortably seats up to four.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/willa-arlo-interiors-affric-glass-dining-table-wlao3771.html",
        "class_name": "Dining Tables",
        "sale_price": 516.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/57526991/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 53.97,
                "y": 53.97,
                "z": 31.1
            },
            "glb": "http://img.wfrcdn.com/docresources/39355/108/1082038.glb",
            "obj": "http://img.wfrcdn.com/docresources/39355/103/1039990.zip"
        }
    },
    {
        "sku": "ACOT3830",
        "product_name": "Gammons End Table",
        "product_description": "Showcasing a pared-down pedestal design and built-in magazine rack, this distinctive end table makes the perfect addition to a smaller space. Set it beside the sofa to corral your favorite reads, and use its surface to display a stylish lamp or rest your morning cup of coffee. A modern structural innovation, this end table has multiple uses without compromising on its style. Fashioned with modern and contemporary accents, the end table is the perfect addition to the interiors of your living area. Carved out of rubber wood and hardwood, the end table is a robust and elegant piece of furniture. The top and base materials are made out of rubber wood and Asian hardwoods with a solid wood construction, elevating the durability of the end table. The solid base of this end table has an anti-wobble feature and provides firm ground support. The back side has an intricately designed and useful magazine holder to store your newspapers, books or magazines. The unique design of the end table allows it to be nestled up against the couch as a drink, snack, remote or book holder. With a slide flush feature, this end table can be faced against the couch. This handy snack table makes an ideal accent piece for the living room, playroom or even bedside.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/alcott-hill-gammons-end-table-acot3830.html",
        "class_name": "End Tables",
        "sale_price": 39.15,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36985/41294247/1/Dartmouth%2BEnd%2BTable.jpg",
        "model": {
            "dimensions_inches": {
                "x": 14.85,
                "y": 11.02,
                "z": 24.01
            },
            "glb": "http://img.wfrcdn.com/docresources/36986/107/1072733.glb",
            "obj": "http://img.wfrcdn.com/docresources/36986/76/764678.zip"
        }
    },
    {
        "sku": "ANDO7174",
        "product_name": "Joseph End Table with Storage",
        "product_description": "Add essential storage to your space without taking up too much square footage with this compact end table. Made from manufactured wood with laminate, this budget-friendly piece strikes a 17.5\" H x 15.5\" W x 15.5\" D silhouette that's perfect beside low sofas or in narrow nooks. Its neutral finish and clean-lined design help it blend with existing arrangements, while its single shelf and drawer provide a place to keep odds and ends. It arrives in a set of two and requires assembly.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-joseph-end-table-with-storage-ando7174.html",
        "class_name": "End Tables",
        "sale_price": 59.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30808/38000800/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 15.5,
                "y": 15.5,
                "z": 17.51
            },
            "glb": "http://img.wfrcdn.com/docresources/30808/106/1065743.glb",
            "obj": "http://img.wfrcdn.com/docresources/30808/86/861902.zip"
        }
    },
    {
        "sku": "ANDO7905",
        "product_name": "Warrington End Table",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-warrington-end-table-ando7905.html",
        "class_name": "End Tables",
        "sale_price": 88.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/47105196/1/furniture%2Fpdp%2Fandover-mills-warrington-end-table.jpg",
        "model": {
            "dimensions_inches": {
                "x": 12,
                "y": 24,
                "z": 24.01
            },
            "glb": "http://img.wfrcdn.com/docresources/31741/107/1079779.glb",
            "obj": "http://img.wfrcdn.com/docresources/31741/97/977719.zip"
        }
    },
    {
        "sku": "ANDV2734",
        "product_name": "Lundgren End Table With Storage ",
        "product_description": "Crafted of solid and manufactured woods available in a selection of fashionable finishes, this versatile end table is a transitional design equipped with modern amenities. One open lower shelf is great for stacking your go-to novels or fanning out your favorite magazines, while one top drawer offers out-of-sight storage for everything from extra batteries to remote controls. A lift-top compartment conceals a charging station with two grounded outlets plus two USB ports so you can always stay connected, while a hidden pull-out tray shelf is great for keeping your coffee or tea on-hand.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-lundgren-end-table-with-storage-andv2734.html",
        "class_name": "End Tables",
        "sale_price": 144.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36681/29389449/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 12.75,
                "y": 22,
                "z": 22.75
            },
            "glb": "http://img.wfrcdn.com/docresources/30808/108/1083759.glb",
            "obj": "http://img.wfrcdn.com/docresources/30808/104/1049071.zip"
        }
    },
    {
        "sku": "ANDV4250",
        "product_name": "Kier End Table",
        "product_description": "A stylish sofa-side accent, this elegant end table will instantly elevate your living room look. While it may seem simplistic at first with its clean-lined wood frame finished in a versatile solid tone, it's what you add on that really makes it all your own! Start with a polished silver lamp to give it a twist of contemporary flair, then lend a little earthy appeal with a small potted succulent. Down below, you'll find an open lower shelf that's ideal for storage space! Try stacking a collection of leather-bound tomes for stately allure, or tuck a woven wicker bin in for a charming spot to stow plush throw blankets and DVDs for movie nights.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-kier-end-table-andv4250.html",
        "class_name": "End Tables",
        "sale_price": 52.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30808/39106492/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 12,
                "y": 24,
                "z": 23.99
            },
            "glb": "http://img.wfrcdn.com/docresources/31741/107/1071401.glb",
            "obj": "http://img.wfrcdn.com/docresources/31741/76/763123.zip"
        }
    },
    {
        "sku": "ANDV4440",
        "product_name": "Creeksville End Table With Storage",
        "product_description": "For the stylish living room in need of just a smidge more storage, this end table ticks the boxes for both form and function. Made from manufactured wood, this piece's three tiers of shelving provide room for everyday essentials, objets d’art, and plants alike, while an x-shaped base lends a contemporary air to any ensemble. Measuring 24'' H x 15.75'' W x 15.75'' D, this compact design works well as an end table in the living room or a bedside table.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-creeksville-end-table-with-storage-andv4440.html",
        "class_name": "End Tables",
        "sale_price": 87.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2445/39533958/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 15.76,
                "y": 15.75,
                "z": 24
            },
            "glb": "http://img.wfrcdn.com/docresources/36986/109/1095288.glb",
            "obj": "http://img.wfrcdn.com/docresources/36986/76/768471.zip"
        }
    },
    {
        "sku": "ATGR2663",
        "product_name": "Kellie End Table",
        "product_description": "Draw the eye to your favorite seating space with this versatile end table, crafted from a mix a wood and manufactured wood. Its curved silhouette adds visual appeal to your decor while its open design brings breezy style to any casual or formal aesthetic. Lean into this piece's country influence by adding it to a den ensemble alongside a pair of linen-upholstered barrel chairs and a streamlined sofa for a casual arrangement, then accent it with a floral-pattern pillow for botanical beauty. Dot nearby walls with whitewash mirrors and farmhouse canvas print for an eye-catching display, then roll out a trellis rug to tie the space together in timeless style. Top this table off with a trio of turned wood candleholders for a touch of traditional style, then pair it with your favorite faux-leather recliner for enjoying your latest read or a glass of after-work wine.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/august-grove-kellie-end-table-atgr2663.html",
        "class_name": "End Tables",
        "sale_price": 94.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37306/26894461/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 17.7,
                "y": 17.7,
                "z": 24
            },
            "glb": "http://img.wfrcdn.com/docresources/37306/109/1096449.glb",
            "obj": "http://img.wfrcdn.com/docresources/37306/102/1022111.zip"
        }
    },
    {
        "sku": "BL12246",
        "product_name": "Keane Side Table",
        "product_description": "Accent your space with vintage charm courtesy of this traditionally styled side table. Its petite frame makes it ideal for the bedside or next to a chair or sofa, and the lower shelf is just the right size for stashing a book.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/birch-lane-keane-side-table-bl12246.html",
        "class_name": "End Tables",
        "sale_price": 138.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/59963301/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 23.54,
                "y": 25.64,
                "z": 30.99
            },
            "glb": "http://img.wfrcdn.com/docresources/25006/127/1273700.glb",
            "obj": "http://img.wfrcdn.com/docresources/25006/127/1279789.zip"
        }
    },
    {
        "sku": "FDLL2143",
        "product_name": "Annable End Table",
        "product_description": "Effortlessly out your ensemble and put your decor on display with this classic end table, the perfect complement for traditional aesthetics.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/fleur-de-lis-living-annable-end-table-fdll2143.html",
        "class_name": "End Tables",
        "sale_price": 162.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/44264/47666465/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 26.02,
                "y": 26.02,
                "z": 26.5
            },
            "glb": "http://img.wfrcdn.com/docresources/39298/106/1069295.glb",
            "obj": "http://img.wfrcdn.com/docresources/39298/76/760755.zip"
        }
    },
    {
        "sku": "GRKS3005",
        "product_name": "Lorraine Global Archive Drum End Table",
        "product_description": "Evocative of a summer-y garden stool, this drum end table is ideal for adding antiqued allure to any indoor ensemble. Crafted from solid mango wood, it takes on a cylindrical silhouette measuring 23\" H by 17\" W by 17\" D. Its rustic solid finish lends a touch of charm, while hand-carved pierced details are what really stand out. Let it shine solo for an artful accent, or add on a potted plant to make it all your own.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/gracie-oaks-lorraine-global-archive-drum-end-table-grks3005.html",
        "class_name": "End Tables",
        "sale_price": 132.3,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2418/40850086/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 17.04,
                "y": 17.04,
                "z": 23.21
            },
            "glb": "http://img.wfrcdn.com/docresources/44304/106/1065369.glb",
            "obj": "http://img.wfrcdn.com/docresources/44304/117/1178222.zip"
        }
    },
    {
        "sku": "GRYL6686",
        "product_name": "Cainsville End Table",
        "product_description": "Prop up potted plants, framed family photos, and a spread of snacks on this clean-lined end table. Right at home in rustic and modern farmhouse arrangements, this piece is crafted with a metal frame and two manufactured wood tiers in a well-worn wood grain finish. Bracket corners and rivet accents bring out this design’s industrial side, while a neutral two-toned finish helps it blend with any existing ensemble. Assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/greyleigh-cainsville-end-table-gryl6686.html",
        "class_name": "End Tables",
        "sale_price": 121.69,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37311/40540407/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 20.18,
                "y": 20.05,
                "z": 19.65
            },
            "glb": "http://img.wfrcdn.com/docresources/37311/107/1071674.glb",
            "obj": "http://img.wfrcdn.com/docresources/37311/76/763408.zip"
        }
    },
    {
        "sku": "LFMF9239",
        "product_name": "Balderston End Table",
        "product_description": "An understated intersection of clean-lined, contemporary aesthetics and rustic simplicity in your environment, this essential end table offers up a touch of subtle style to your aesthetic. Featuring a boxy, openwork particle board design, this end table is the definition of low-key, while its lower shelf lets you double up on its display possibilities. Use the top to stage a glowing table lamp next to your living room sofa, then utilize the lower shelf to arrange stacked art books or a basket of remotes. Looking to switch things up in the master suite? This end table makes n unexpected and simple nightstand alternative!",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/balderston-end-table-lfmf9239.html",
        "class_name": "End Tables",
        "sale_price": 79.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37311/51225744/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 24,
                "y": 12,
                "z": 22
            },
            "glb": "http://img.wfrcdn.com/docresources/13685/109/1090670.glb",
            "obj": "http://img.wfrcdn.com/docresources/13685/101/1017770.zip"
        }
    },
    {
        "sku": "LMDW1045",
        "product_name": "Altitude End Table With Storage",
        "product_description": "Offer clean-lined style and effortless utility to any seating group or entertainment ensemble with this understated chairside table, the perfect blend of low-key looks and simple versatility. Featuring two tiers of shelving, this Altitude End Table With Storage makes a stylish stage for any display. Set it next to a linen-upholstered loveseat in the living room to complement its cherry-finished wood design, Use the lower shelf to stack art books and hardcover novels, then top it off with a blooming faux floral bouquet or glowing table lamp to round out the look.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/charlton-home-altitude-end-table-with-storage-lmdw1045.html",
        "class_name": "End Tables",
        "sale_price": 116.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/41179199/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 14.28,
                "y": 21.62,
                "z": 23.93
            },
            "glb": "http://img.wfrcdn.com/docresources/36986/107/1072442.glb",
            "obj": "http://img.wfrcdn.com/docresources/36986/76/764299.zip"
        }
    },
    {
        "sku": "QSI2845",
        "product_name": "Warm Shaker End Table with Storage",
        "product_description": "The Simpli Home Warm Shaker End Table is a spacious and useful table with one exterior shelf and one large bottom drawer for additional storage. It is rectangular in shape and is sturdy enough to bear weight of 50 pounds. Designed in a contemporary style, this table can be paired easily with any modern or traditional living room set or can be used as a bedside table. The protective NC lacquer finish ensures that this table can be used for regular purposes without fear of scratch or stain. You can display a lamp or other memorabilia on the spacious top. There is one more exterior shelf located just below the top which is great for additional storage or display. This table has a large drawer in the bottom which glides easily on metal extensions. It has a shaker style drawer front and is mounted with rounded rectangular brush nickel knob. You can keep odds and ends here and make your room clutter free.  This eco-friendly table should be wiped clean with a dry cloth for proper maintenance.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/simpli-home-warm-shaker-end-table-qsi2845.html",
        "class_name": "End Tables",
        "sale_price": 131.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/34591/35163484/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 20,
                "y": 18,
                "z": 19.41
            },
            "glb": "http://img.wfrcdn.com/docresources/36985/108/1081681.glb",
            "obj": "http://img.wfrcdn.com/docresources/36985/103/1036703.zip"
        }
    },
    {
        "sku": "TADN3619",
        "product_name": "Cimarron End Table",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/trent-austin-design-cimarron-end-table-tadn3619.html",
        "class_name": "End Tables",
        "sale_price": 132.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/37312/57862491/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 13.89,
                "y": 13.89,
                "z": 17.7
            },
            "glb": "http://img.wfrcdn.com/docresources/37312/128/1284033.glb",
            "obj": "http://img.wfrcdn.com/docresources/37312/129/1290262.zip"
        }
    },
    {
        "sku": "WDLN2091",
        "product_name": "Farmingdale End Table",
        "product_description": "Round out your favorite seating space in sophisticated flair with this metal and glass end table. Rounded upon four acrylic legs and showcasing a tempered glass top, this sleek design is sure to spark conversation. Add this end table to your living room to anchor a contemporary ensemble alongside a track arm sofa and complementing arm chairs for a cohesive and on-trend arrangement. This table's clean top is the perfect canvas for an array of framed family photos or a trio of sculpted metal statuettes for visual appeal. Equally stylish and functional, this angular end table ups the ante of your favorite aesthetic.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/wade-logan-farmingdale-end-table-wdln2091.html",
        "class_name": "End Tables",
        "sale_price": 208.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/46533576/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 24.06,
                "y": 24.06,
                "z": 24.14
            },
            "glb": "http://img.wfrcdn.com/docresources/44325/106/1067636.glb",
            "obj": "http://img.wfrcdn.com/docresources/44325/87/875112.zip"
        }
    },
    {
        "sku": "ZIPC1758",
        "product_name": "Kathleen End Table With Storage",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-kathleen-end-table-with-storage-zipc1758.html",
        "class_name": "End Tables",
        "sale_price": 95.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30593/58423724/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 18.9,
                "y": 15.79,
                "z": 25.79
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/125/1259679.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/126/1264210.zip"
        }
    },
    {
        "sku": "ZPCD2910",
        "product_name": "Castillo End Table",
        "product_description": "With this C-shaped end table, bringing storage, style, and functionality to your seating group is as easy as A,B…see? Measuring just 25.3'' H x 10'' W x 16'' D, this table makes the most of your square footage and pulls up snug to sofas, armchairs, and more. Its clean-lined frame is crafted from metal and finished in gold, and the top is fitted with glass. It offers a convenient spot to place your laptop, set down a cup of coffee, display a bloom-filled vase – you name it!",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-castillo-end-table-zpcd2910.html",
        "class_name": "End Tables",
        "sale_price": 71.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36987/37450023/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 10,
                "y": 16,
                "z": 25.3
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/106/1067783.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/89/896582.zip"
        }
    },
    {
        "sku": "ZPCD5938",
        "product_name": "Colleen End Table with Storage",
        "product_description": "End Table Corner Shelves.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-colleen-end-table-with-storage-zpcd5938.html",
        "class_name": "End Tables",
        "sale_price": 38.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/42689/55978022/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 13.4,
                "y": 13.4,
                "z": 20
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/116/1169161.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/117/1177029.zip"
        }
    },
    {
        "sku": "ZPCD6199",
        "product_name": "Crow End Table",
        "product_description": "This Round End Table is a great fit for your modern simple lifestyle. The beautiful color fits any room in your home. It can be put beside your sofa, your bed, or anywhere you want an end table to provide some storage and display for your handy needs. Space saving and sturdy. The main material - medium density composite wood is manufactured in Malaysia and complied with the green rules of production. There is no foul smell, durable and the material is the most stable amongst the medium density composite woods. A simple attitude towards lifestyle is reflected directly on the design of this manufacturer, creating a trend of simply nature. All the products are produced and assembled 100% in Malaysia with 95% - 100% recycled materials. Care instructions wipe clean with clean damped cloth. Avoid using harsh chemicals. Pictures are for illustration purpose. All decor items are not included in this offer.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-crow-end-table-zpcd6199.html",
        "class_name": "End Tables",
        "sale_price": 53.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30593/54978742/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 18.98,
                "y": 15.45,
                "z": 19.44
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/110/1106238.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/113/1135379.zip"
        }
    },
    {
        "sku": "CHRH6150",
        "product_name": "Crisfield Kitchen Island",
        "product_description": "Sometimes feel like you could use a sidekick in the kitchen? This all-in-one island is here to help! Whether you're whipping up delectable desserts for a bake sale at the kids' school or setting out appetizers before the main meal at your next dinner party, it's an essential to have on hand. Founded atop four castered wheels for effortless mobility wherever you need it, its clean-lined frame is crafted of wood with a chocolate finish that beautifully blends into any abode. Use the gray oak-finished top to prepare the ingredients for your famous fudge brownies, then get cleaned up in a pinch by keeping a towel draped over the side rack and placing your baking supplies inside its two cabinets and single drawer up top. When it's not in use, simply use it as a centerpiece for the heart of your home with a flat-woven rug laying out underneath and a vase of freshly-picked hydrangeas dotting the top.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/charlton-home-crisfield-kitchen-island-chrh6150.html",
        "class_name": "Kitchen Islands",
        "sale_price": 120.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36986/57295233/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 45,
                "y": 15.55,
                "z": 34.91
            },
            "glb": "http://img.wfrcdn.com/docresources/36986/107/1072684.glb",
            "obj": "http://img.wfrcdn.com/docresources/36986/76/764602.zip"
        }
    },
    {
        "sku": "DRBH8022",
        "product_name": "Chan Kitchen Island with Stainless Steel Top",
        "product_description": "Timeless and traditional, this kitchen island with a stainless steel top is perfect for specialty storage and pre-dinner prep work. Available in a selection of classic finishes, the vanity base is crafted of solid and manufactured wood and features tasteful moldings, raised panel details, and four locking wheel feet. Two drawers run on metal glides to offer out-of-sight storage for essential entertaining utensils, while four doors open to three separate cabinets with shelved storage for all your serveware and specialty appliances. A natural wood counter offers a contemporary contrast, while a built-in spice and towel rack round out the design.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/darby-home-co-chan-kitchen-island-with-stainless-steel-top-drbh8022.html",
        "class_name": "Kitchen Islands",
        "sale_price": 308.24,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36984/17826832/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 52,
                "y": 18,
                "z": 36
            },
            "glb": "http://img.wfrcdn.com/docresources/36984/120/1200844.glb",
            "obj": "http://img.wfrcdn.com/docresources/36984/121/1215555.zip"
        }
    },
    {
        "sku": "LOON6775",
        "product_name": "Lockwood Kitchen Island with Ceramic Tile Top and Stools",
        "product_description": "Handcrafted solid wood and wood veneer kitchen island set with decorative accents. Set includes two Windsor Style Comfort back swivel stools with curved back support, scooped seat and steel reinforced turned legs. The uniquely designed island offers a ceramic tile sliding countertop with three adjustable locking positions: centered over island base, left side overhang or right side overhang. OThis adaptable island instantly converts to meet your quick-changing lifestyle needs. One spacious large drawer for dining linens and utensils. Two doors underneath open to one adjustable shelf for convenient access and storage of cookware and other large kitchen/entertaining items. Three open fixed shelves for prominent display of decorative mixing bowls, baskets or gourmet cookware. Four attractive bun feet at bottom of base.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/loon-peak-lockwood-kitchen-island-with-ceramic-tile-top-and-stools-loon6775.html",
        "class_name": "Kitchen Islands",
        "sale_price": 1499.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58460823/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 60,
                "y": 44.92,
                "z": 44.33
            },
            "glb": "http://img.wfrcdn.com/docresources/37311/118/1181560.glb",
            "obj": "http://img.wfrcdn.com/docresources/37311/118/1186141.zip"
        }
    },
    {
        "sku": "LRFY8074",
        "product_name": "Fresnay Kitchen Island with Wooden Top",
        "product_description": "Providing a bit of extra pantry space, this versatile kitchen island brings function to the heart of your home without sacrificing style. Crafted with an iron frame, this rustic piece features a distressed MDF countertop and two lower shelves that support up to 80 pounds of serveware, canned foods, and more. Its removable wire baskets offer a dash of factory flair, while rolling casters down below let you move this design around the room. Assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/fresnay-kitchen-island-with-wooden-top-lrfy8074.html",
        "class_name": "Kitchen Islands",
        "sale_price": 194.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/47541763/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 47.43,
                "y": 17,
                "z": 31.29
            },
            "glb": "http://img.wfrcdn.com/docresources/2294/107/1070389.glb",
            "obj": "http://img.wfrcdn.com/docresources/2294/90/901712.zip"
        }
    },
    {
        "sku": "ONAW3697",
        "product_name": "Benedetto Kitchen Island with Door",
        "product_description": "This Benedetto Kitchen Island with Door features two pass-through drawers allowing accessibility on either side, two doors with adjustable shelving, additional adjustable shelving on ends, casters for mobility. Hand-applied distressed transparent finish. Tongue and groove construction on top, pine solids on rest of units. Hardware consist of nostalgic cup pulls finished in a dark antique brass.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/one-allium-way-benedetto-kitchen-island-with-door-onaw3697.html",
        "class_name": "Kitchen Islands",
        "sale_price": 631.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/58359988/1/furniture%2Fpdp%2Fone-allium-way-benedetto-kitchen-island-with-door.jpg",
        "model": {
            "dimensions_inches": {
                "x": 48,
                "y": 24,
                "z": 34.78
            },
            "glb": "http://img.wfrcdn.com/docresources/37307/120/1200838.glb",
            "obj": "http://img.wfrcdn.com/docresources/37307/121/1215571.zip"
        }
    },
    {
        "sku": "RBSD3661",
        "product_name": "Auden Kitchen Cart with Faux Marble Top",
        "product_description": "Alright, you need to whip up brownies for the bake sale, put together tonight's dinner, and prep a cheeseboard for tomorrow night's cocktail party... you've got a lot on your plate, and this kitchen cart can help. Measuring 34'' H x 32'' W x 16'' D, its mobile wood frame features a cabinet, drawer, and three shelves to keep everything you need on hand. Plus, a marble top is perfect for chopping and serving. See? You've got this.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/red-barrel-studio-auden-kitchen-cart-with-faux-marble-top-rbsd3661.html",
        "class_name": "Kitchen Islands",
        "sale_price": 182.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/54988339/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 32.13,
                "y": 16.29,
                "z": 33.9
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/112/1121524.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/113/1139125.zip"
        }
    },
    {
        "sku": "STSS5834",
        "product_name": "Shounak Kitchen Cart",
        "product_description": "Be inspired with this Shounak Kitchen Cart industrial design that uses mixed media materials. Delivered to your door by parcel post service.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/17-stories-shounak-kitchen-cart-stss5834.html",
        "class_name": "Kitchen Islands",
        "sale_price": 384.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58465479/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 46.75,
                "y": 20,
                "z": 36
            },
            "glb": "http://img.wfrcdn.com/docresources/44315/118/1182267.glb",
            "obj": "http://img.wfrcdn.com/docresources/44315/120/1202121.zip"
        }
    },
    {
        "sku": "TRNT3442",
        "product_name": "Haleakal Kitchen Island with Butcher Block Top",
        "product_description": "No kitchen island? No problem! Forget the contractor and add a centerpiece to the heart of your home in seconds with this freestanding design. Perfect for both classic and contemporary ensembles, it pairs a stainless steel base with a hardwood butcher block top. Measuring 36'' H x 52'' W x 25'' D, it offers space to work and serve on top, while two tiers of slatted shelving below let you stow.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/trent-austin-design-haleakal-kitchen-island-with-butcher-block-top-trnt3442.html",
        "class_name": "Kitchen Islands",
        "sale_price": 417.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/58417112/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 52,
                "y": 25,
                "z": 35.99
            },
            "glb": "http://img.wfrcdn.com/docresources/37312/116/1161468.glb",
            "obj": "http://img.wfrcdn.com/docresources/37312/117/1176762.zip"
        }
    },
    {
        "sku": "TRPT2276",
        "product_name": "Fitzhugh Kitchen Island",
        "product_description": "Showcasing a stainless steel surface and 2 slatted shelves, this rolling island makes a versatile addition to your kitchen ensemble. Pull it up to the counter for extra food prep space and ingredient storage, then use it as a convenient buffet when guests arrive.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-fitzhugh-kitchen-island-trpt2276.html",
        "class_name": "Kitchen Islands",
        "sale_price": 384.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/52559955/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 47.12,
                "y": 20.51,
                "z": 35.99
            },
            "glb": "http://img.wfrcdn.com/docresources/36984/109/1090030.glb",
            "obj": "http://img.wfrcdn.com/docresources/36984/101/1013258.zip"
        }
    },
    {
        "sku": "ALCT4979",
        "product_name": "Leesburg Big Swirl Cocktail Ottoman",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/alcott-hill-leesburg-big-swirl-cocktail-ottoman-alct4979.html",
        "class_name": "Ottomans",
        "sale_price": 352.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36985/27645919/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 40.99,
                "y": 41,
                "z": 20
            },
            "glb": "http://img.wfrcdn.com/docresources/36985/109/1090179.glb",
            "obj": "http://img.wfrcdn.com/docresources/36985/101/1014952.zip"
        }
    },
    {
        "sku": "ANDO7575",
        "product_name": "Rockville Storage Ottoman",
        "product_description": "The perfect balance of clean-lined looks and simple utility in your well-curated and welcoming environment, this striking storage ottoman makes a simply chic addition to your space. Featuring a boxy wood and plastic design wrapped in polyester and faux leather, this storage ottoman is a stately, yet unfussy addition to your look, while the gently stitched, button-tufted top adds a dash of definition and character to the piece. Add it to your living room seating group to effortlessly complement aesthetics both traditional and today, then lift up the seat to stow away spare blankets, board games, and more in effortless style.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-rockville-storage-ottoman-ando7575.html",
        "class_name": "Ottomans",
        "sale_price": 30.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30808/38883532/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 15,
                "y": 15,
                "z": 15.03
            },
            "glb": "http://img.wfrcdn.com/docresources/33866/107/1072440.glb",
            "obj": "http://img.wfrcdn.com/docresources/33866/76/764298.zip"
        }
    },
    {
        "sku": "ANDV2297",
        "product_name": "Mullenax Storage Ottoman",
        "product_description": "Ready for an impromptu movie night? Don't lose time corralling cozy pieces and searching for that favorite flick! Keep everything you need for the evening right on hand every time with this alluring ottoman. Founded atop four tapered block feet, its frame is crafted of solid wood and features faux leather upholstery in a versatile solid hue for a look that beautifully blends into any ensemble. Lift the top and you'll find storage space, perfect for tucking away your DVD collection and plenty of plush blankets. Even if you're not much of a film fiend, you can always use this design as a centerpiece awaiting trays of tapas and sangria while you entertain.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/andover-mills-mullenax-storage-ottoman-andv2297.html",
        "class_name": "Ottomans",
        "sale_price": 364.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/47149689/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 49.03,
                "y": 32,
                "z": 16.5
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/108/1082192.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/102/1025594.zip"
        }
    },
    {
        "sku": "BCMH4335",
        "product_name": "Nobles Storage Ottoman",
        "product_description": "Center your seating arrangement around style, and add essential storage space to your ensemble, with this lovely ottoman. A contemporary design with a touch of the tropics, it showcases a rounded frame plywood with four flared legs crafted from solid wood legs. The frame is wrapped in woven banana leaf, so you can round out your room with a touch of texture. The top can be removed to reveal hidden storage within.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/beachcrest-home-nobles-storage-ottoman-bcmh4335.html",
        "class_name": "Ottomans",
        "sale_price": 173.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/48727690/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 18,
                "y": 15.06,
                "z": 16.5
            },
            "glb": "http://img.wfrcdn.com/docresources/24040/108/1082940.glb",
            "obj": "http://img.wfrcdn.com/docresources/24040/104/1046015.zip"
        }
    },
    {
        "sku": "BKWT1443",
        "product_name": "Baffin Cube Ottoman",
        "product_description": "This Baffin Pouf features an attractive look, and it is practical to use. Perfect to use outdoors, this ottoman is highly durable to use all round the year. This Baffin Pouf has 50-percent recycled polystyrene beads that make it durable and comfortable to use. This ottoman is woven with outdoor treated polyester, which makes it durable and perfect for outdoor use. It has striped pattern and square shape that looks charming and adds elegance to its contemporary style. It is available in multiple colors that give you several options to select your favorite color. It is water-resistant, which makes it perfect to use in all weather conditions. This ottoman is resistant to fading, rusting, and mildewing. It is equally suited to use this ottoman for indoor, outdoor, and commercial use. It has the capacity to hold weight up to 300 pounds. This stylish and well-designed ottoman is practical to use as a chair, footstool, or side table, and looks attractive as an outdoor ottoman in the patio, lawn, or garden. This stylish ottoman is eco-friendly, which makes it equally suitable for both indoor and outdoor use. It can be machine washed gently with cool water.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/breakwater-bay-baffin-cube-ottoman-bkwt1443.html",
        "class_name": "Ottomans",
        "sale_price": 72.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/38454/39211793/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 17.01,
                "y": 17.01,
                "z": 16.81
            },
            "glb": "http://img.wfrcdn.com/docresources/38454/128/1288825.glb",
            "obj": "http://img.wfrcdn.com/docresources/38454/129/1293956.zip"
        }
    },
    {
        "sku": "DABH1785",
        "product_name": "Groner Cocktail Ottoman",
        "product_description": "Doubling as a spot to sit and a convenient place to set down a spread of magazines, this versatile oval ottoman is equal parts function and style. This generously sized piece is built with a hardwood and plywood frame, filled with high-density foam, and upholstered with linen-hued polyester fabric that resists fading and wrinkling. The dark espresso finish on its six solid birch legs gives it a touch of warmth, while button-tufted details on its cushion round out the design. After assembly, it supports up to 250 lbs.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/darby-home-co-groner-cocktail-ottoman-dabh1785.html",
        "class_name": "Ottomans",
        "sale_price": 175.79,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/47656000/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 48,
                "y": 27.5,
                "z": 18.2
            },
            "glb": "http://img.wfrcdn.com/docresources/36984/107/1079536.glb",
            "obj": "http://img.wfrcdn.com/docresources/36984/98/981575.zip"
        }
    },
    {
        "sku": "LARK2659",
        "product_name": "Sirine Ottoman",
        "product_description": "Ottomans aren't only for kicking your feet up – they also provide the perfect perch for a tray, offer extra guest seating, and just add style to your space overall! This one, for example, is an ideal addition to any living room look or master suite ensemble. Crafted from solid and manufactured wood, its frame features cabriole legs and a curved apron all finished in natural brown. Up top, the cushion is wrapped in polyester blend upholstery with tufts for added traditional appeal.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/lark-manor-sirine-ottoman-lark2659.html",
        "class_name": "Ottomans",
        "sale_price": 154.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37152/31221264/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 24,
                "y": 23.99,
                "z": 16.5
            },
            "glb": "http://img.wfrcdn.com/docresources/37152/108/1087213.glb",
            "obj": "http://img.wfrcdn.com/docresources/37152/98/989943.zip"
        }
    },
    {
        "sku": "LATR4418",
        "product_name": "Neil Storage Ottoman",
        "product_description": "The spot where storage space meets style, this ottoman makes an ideal anchor for your living room look or an eye-catching accent at the foot of your bed. Its birch wood frame is founded atop four tapered block feet, all finished in brown for versatility. Up top, polyester blend upholstery wraps around the piece with a scrolling floral motif in hues of cream, turquoise, brown and aquamarine. Whether you're stowing blankets, shoes or anything in between, all you need to do is lift the hinged lid to reveal a hollow inside.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/latitude-run-neil-storage-ottoman-latr4418.html",
        "class_name": "Ottomans",
        "sale_price": 118.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/58424611/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 38,
                "y": 19,
                "z": 16
            },
            "glb": "http://img.wfrcdn.com/docresources/40128/118/1180538.glb",
            "obj": "http://img.wfrcdn.com/docresources/40128/118/1184722.zip"
        }
    },
    {
        "sku": "LFMF4589",
        "product_name": "Barkell Cocktail Ottoman",
        "product_description": "Make a statement with this Cocktail Ottoman. Featuring a Walnut faux leather cushion top, paired with a nail head trim. Also featuring a slatted bottom shelf for additional storage. Whether you use this bench in the living room as a main piece or in the entryway to welcome guests this piece will not disappoint.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/barkell-cocktail-ottoman-lfmf4589.html",
        "class_name": "Ottomans",
        "sale_price": 249.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37311/18113428/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 43,
                "y": 23,
                "z": 17.99
            },
            "glb": "http://img.wfrcdn.com/docresources/37311/109/1091563.glb",
            "obj": "http://img.wfrcdn.com/docresources/37311/76/765808.zip"
        }
    },
    {
        "sku": "LGLY6746",
        "product_name": "Janeen Cocktail Ottoman",
        "product_description": "Add a contemporary touch to the center of your seating space with this lovely cocktail ottoman. Taking inspiration from midcentury designs, it showcases a square frame supported by four tapered rubberwood legs. The 100% polyester upholstery is available in a variety of colors, while the legs are finishes with a black stain. The top features button tufts for a touch of dimension, and it is stuffed with dense foam padding.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-janeen-cocktail-ottoman-lgly6746.html",
        "class_name": "Ottomans",
        "sale_price": 189.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36991/36935586/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 35.5,
                "y": 35.5,
                "z": 17.5
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/108/1082307.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/104/1042953.zip"
        }
    },
    {
        "sku": "MCRF4356",
        "product_name": "Norfolk Ottoman",
        "product_description": "You'll be sitting pretty on this Norfolk Ottoman. This beautiful piece has a stunning look with its velvet upholstery and nailhead trim that gives your room a decidedly contemporary vibe. The X-shaped legs are sturdy and stout, making it a beautifully durable addition to your space. The ottoman's large top accommodates your feet while you relax and unwind with a good book, or pull it out on game night for an extra seat.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercer41-norfolk-ottoman-mcrf4356.html",
        "class_name": "Ottomans",
        "sale_price": 107.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36892/43417832/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 20.33,
                "y": 20.55,
                "z": 19.44
            },
            "glb": "http://img.wfrcdn.com/docresources/39355/120/1201673.glb",
            "obj": "http://img.wfrcdn.com/docresources/39355/121/1216253.zip"
        }
    },
    {
        "sku": "MCRW5934",
        "product_name": "Coggin Ottoman",
        "product_description": "Searching for a stylish seat? Look no further than this alluring ottoman - an unexpected alternative to your average chair or chaise. Try sitting it in a sunny corner of the living room to complement your contemporary seating ensemble, or bring it right into the fold when you need to stage a tray of delectable drinks at your next cocktail party with friends. Founded atop four slanted legs, its frame is crafted of manufactured wood with an angled top wrapped in tufted upholstery with polished chrome nailhead trim along the edges.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mercury-row-coggin-ottoman-mcrw5934.html",
        "class_name": "Ottomans",
        "sale_price": 87.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36991/37552815/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 35.95,
                "y": 17.97,
                "z": 18.5
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/108/1087375.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/99/998973.zip"
        }
    },
    {
        "sku": "MTNA2948",
        "product_name": "Grimes Pouf",
        "product_description": "Handcrafted from polystyrene, this chunky knit poof effortlessly adds a pop of texture to your well-appointed ensemble. To easily incorporate this design into a boho-chic ensemble, roll out a gray overdyed area rug to anchor the space, then place this pouf between a reclaimed wood coffee table and a slipper chair with bright, floral medallion upholstery. Add a button-tufted chesterfield sofa and a dark wood end table with abalone inlays to round out the arrangement, and accessorize the space in global-inspired style with tribal pattern accent pillows, an ikat throw blanket, and a lacy embroidered coffee table runner. Hosting a viewing party for a livestream of your favorite music festival? Add more of these poufs to the ensemble for extra seating, then set out snacks and a pitcher of sangria and sing along to the song of the summer with your besties.   ",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mistana-grimes-pouf-mtna2948.html",
        "class_name": "Ottomans",
        "sale_price": 80.79,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/44356/59431782/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 20,
                "y": 20,
                "z": 14
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/106/1068511.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/75/758963.zip"
        }
    },
    {
        "sku": "RBRS6648",
        "product_name": "Parksley Storage Ottoman",
        "product_description": "Your sidekick in comfort, this storage ottoman lets you kick your feet up and keep cozy blankets nearby. Founded atop four straight legs, its base is crafted from solid birch wood and features a dark solid finish. <br/>Up top, you'll find 100% polyester upholstery with a cool blue hue and button tufts, while a lower shelf offers storage and display options below. Overall, this circular design measures 20'' H x 36'' W x 36'' D.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/red-barrel-studio-parksley-storage-ottoman-rbrs6648.html",
        "class_name": "Ottomans",
        "sale_price": 279.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/57685485/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 36.15,
                "y": 36.15,
                "z": 20.01
            },
            "glb": "http://img.wfrcdn.com/docresources/34591/109/1097145.glb",
            "obj": "http://img.wfrcdn.com/docresources/34591/109/1097146.zip"
        }
    },
    {
        "sku": "THRE3819",
        "product_name": "Scipio Ottoman",
        "product_description": "Add a plush touch to the parlor or master suite with this chic tufted ottoman! Founded on a sturdy hardwood frame with four ebony turned legs, this dapper design strikes a plush rectangular silhouette measuring 19'' H x 28.4'' W x 18'' D overall. Brushed cotton upholstery envelops the ottoman and padded pillowtop cushion, while deep button-tufts, detail stitching, and piped edges offer a tailored touch. With a 250 lbs. weight capacity, this piece can be used to prop up your feet while watching a movie, or set as extra seating at your next soiree.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-scipio-ottoman-thre3819.html",
        "class_name": "Ottomans",
        "sale_price": 90.39,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/59095933/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 28,
                "y": 19,
                "z": 17.96
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/131/1312183.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/131/1315586.zip"
        }
    },
    {
        "sku": "TRNT5129",
        "product_name": "Sigler Cocktail Ottoman",
        "product_description": "Whether you’re resting your feet or looking for an extra seat, this ottoman delivers! Measuring 18.5'' H x 35.5'' W x 35.5'' D, its oversize manufactured birch frame offers space aplenty for feet, snack trays, weary behinds, and beyond, while espresso-hued upholstery lends a touch of understated style to this living room must-have. Nailhead detailing around the lower edge adds another layer of contemporary flair. For comfort, the top is filled with high-density foam.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/trent-austin-design-sigler-cocktail-ottoman-trnt5129.html",
        "class_name": "Ottomans",
        "sale_price": 213.29,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/58055944/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 35.02,
                "y": 35.02,
                "z": 17.95
            },
            "glb": "http://img.wfrcdn.com/docresources/37312/121/1219159.glb",
            "obj": "http://img.wfrcdn.com/docresources/37312/122/1222653.zip"
        }
    },
    {
        "sku": "TRPT1526",
        "product_name": "Harbison Mid Storage Ottoman",
        "product_description": "An updated version of a living room staple, this stylishly square storage ottoman blends traditional appeal with contemporary convenience. Made with a solid walnut frame in a rich, dark stain, this dapper design showcases slubby fabric upholstery in a blue-and-gray paisley print. Perfect for stowing away extra pillows, throw blankets, coasters or remotes, a hinged lid with classic corded edges opens to reveal a surreptitious storage space. For the perfect movie-watching arrangement in your open-concept living room, start by rolling out an ornate area rug to define the space, then place this charming ottoman between a button-tufted chesterfield armchair and a simple oak console table topped with a sleek flat screen TV. Chilly night? Pull out a chunky-knit throw from this storage ottoman, then kick back, snuggle up, and stream the latest blockbuster.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-harbison-mid-storage-ottoman-trpt1526.html",
        "class_name": "Ottomans",
        "sale_price": 65.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/42381875/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 17.51,
                "y": 17.45,
                "z": 16.5
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/106/1065981.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/86/864334.zip"
        }
    },
    {
        "sku": "TRPT5720",
        "product_name": "Hobgood Deluxe Storage Ottoman",
        "product_description": "Storage space meets style in this eye-catching ottoman, an ideal addition to any entryway or living room look. Founded atop four turned feet, its frame is crafted from hardwood and measures 18'' H x 43'' W x 22'' D overall. Non-fussy faux leather upholstery in a neutral espresso hue wraps around to tie it all together, while button tufts along the lift top make this piece a fine fit for traditional aesthetics.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-hobgood-deluxe-storage-ottoman-trpt5720.html",
        "class_name": "Ottomans",
        "sale_price": 131.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/61388427/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 43,
                "y": 22,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/34834/129/1298141.glb",
            "obj": "http://img.wfrcdn.com/docresources/34834/130/1307676.zip"
        }
    },
    {
        "sku": "WRLO5951",
        "product_name": "Blakesley Ottoman",
        "product_description": "Upholstered in beautiful fabric and lined with sophisticated nailhead trim, this Blakesley Ottoman makes the perfect perch for your feet in the living room or a tray of cocktails and snacks in the guest suite.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/willa-arlo-interiors-blakesley-ottoman-wrlo5951.html",
        "class_name": "Ottomans",
        "sale_price": 236.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/428/11295295/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 34.52,
                "y": 34.21,
                "z": 20.5
            },
            "glb": "http://img.wfrcdn.com/docresources/428/107/1075969.glb",
            "obj": "http://img.wfrcdn.com/docresources/428/92/926080.zip"
        }
    },
    {
        "sku": "ZPCD6679",
        "product_name": "Salazar Storage Ottoman",
        "product_description": "Fashionable, functional, and fun, this on-trend storage ottoman is a tasteful triple threat. Crafted with a solid rubberwood frame, this compact piece measures just 18'' H x 17'' W x 17'' D to fit easily in smaller spaces. Its polyester-blend upholstery showcases a contemporary geometric motif for a pop of pattern, while its hinged lid lifts to reveal a convenient compartment to stash spare blankets, magazines, and more. With a weight capacity of 250 lbs., this versatile design can also double as an extra seat. Some assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-salazar-storage-ottoman-zpcd6679.html",
        "class_name": "Ottomans",
        "sale_price": 59.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/52067915/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 17.04,
                "y": 17.04,
                "z": 18.02
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/108/1085622.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/108/1085623.zip"
        }
    },
    {
        "sku": "ALCT3246",
        "product_name": "Huntsville Sofa",
        "product_description": "A contemporary update on a traditional silhouette, this versatile Huntsville Sofa sets a transitional foundation in your living room. Founded atop four espresso-finished plastic feet, this budget-friendly piece is crafted in the USA with a wooden frame, foam fill, and coil spring supports for a medium-firm feel. Its solid-hued polyester faux suede upholstery contributes to its understated look, while flared pillowtop arms and a pillow back enhance its inviting appeal. Minimal assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/alcott-hill-huntsville-sofa-alct3246.html",
        "class_name": "Sofas",
        "sale_price": 420.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36985/22966747/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 89,
                "y": 39.08,
                "z": 40.1
            },
            "glb": "http://img.wfrcdn.com/docresources/36985/107/1071250.glb",
            "obj": "http://img.wfrcdn.com/docresources/36985/107/1071251.zip"
        }
    },
    {
        "sku": "ALTH1429",
        "product_name": "Garner Chesterfield Settee",
        "product_description": "Defined by its iconic Chesterfield silhouette, this settee brings a hint of classic character to any room in your home. Founded atop four wooden legs finished in espresso, this piece is crafted with a solid birch frame, web suspension seating, and sinuous spring supports to offer a medium seating firmness. Solid-hued, 100% linen fabric envelops the design for understated appeal, while button-tufted details dot the back and seat for a touch of texture. Assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/alcott-hill-garner-chesterfield-settee-alth1429.html",
        "class_name": "Sofas",
        "sale_price": 389.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36985/42608126/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 57,
                "y": 30,
                "z": 31.89
            },
            "glb": "http://img.wfrcdn.com/docresources/36985/108/1084218.glb",
            "obj": "http://img.wfrcdn.com/docresources/36985/108/1084219.zip"
        }
    },
    {
        "sku": "CSTM2191",
        "product_name": "Avery Sleeper Sofa",
        "product_description": "This sleeper sofa showcases a contemporary look that works with a variety of aesthetics. Its crisp track arms, square cushions, and block feet create a clean-lined silhouette that gives your living room a tailored update. Founded atop a manufactured wood frame, it features foam cushions and a queen-size innerspring mattress that pulls out to easily accommodate overnight guests. Its removable cushion covers are simple to clean: just pop them in the washing machine. Plus, it's made in the USA!",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/avery-sleeper-sofa-cstm2191.html",
        "class_name": "Sofas",
        "sale_price": 1049,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/29727/41063865/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 86.12,
                "y": 39,
                "z": 34.05
            },
            "glb": "http://img.wfrcdn.com/docresources/29727/109/1090136.glb",
            "obj": "http://img.wfrcdn.com/docresources/29727/105/1054810.zip"
        }
    },
    {
        "sku": "CSTM2247",
        "product_name": "Harper Sofa",
        "product_description": "Featuring a subtly button-tufted back, tapered wood legs, and bolster pillows, this understated sofa lends a simply chic touch to your parlor or living room ensemble.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/harper-sofa-cstm2247.html",
        "class_name": "Sofas",
        "sale_price": 829,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/29727/41068145/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 86,
                "y": 37,
                "z": 32
            },
            "glb": "http://img.wfrcdn.com/docresources/29727/109/1096416.glb",
            "obj": "http://img.wfrcdn.com/docresources/29727/109/1096417.zip"
        }
    },
    {
        "sku": "LGLY3037",
        "product_name": "Del Lago Ivy Sofa",
        "product_description": "Add a touch of contemporary style to your living room or parlor ensemble with this understated sofa, featuring a clean-lined silhouette and tapered, brown-finished legs.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-del-lago-ivy-sofa-lgly3037.html",
        "class_name": "Sofas",
        "sale_price": 573.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/33807/38701897/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 88.42,
                "y": 37.6,
                "z": 38.82
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/125/1258918.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/126/1263840.zip"
        }
    },
    {
        "sku": "LGLY3103",
        "product_name": "Tucson 39.5\" Loveseat",
        "product_description": "With its mid-century modern look and space-conscious design, there’s not much we DON’T love about this loveseat. The back and seat cushion are wrapped in faux leather upholstery and finished with square-stitch details, while a brown rubberwood frame rounds out the appearance with a touch of warmth. Both cushions are padded with foam, and the seat cushion removes for easy cleaning. If you’re looking to sit two in style, this loveseat is a perfect pick.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-tucson-395-loveseat-lgly3103.html",
        "class_name": "Sofas",
        "sale_price": 258.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36991/38047858/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 44.77,
                "y": 29.25,
                "z": 31.28
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/82/820743.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/76/765820.zip"
        }
    },
    {
        "sku": "LGLY5819",
        "product_name": "Martinique Tufted Sofa",
        "product_description": "Brimming with the mid-century appeal, this wow-worthy Martinique Tufted Sofa is sure to draw the eye to your well-appointed furniture arrangement. Its tufted details add a refined touch to your decor, while its deep seating and curved arms add visual flair to any space. Lean into this piece's mod inspiration by adding it to a living room ensemble alongside complementing wingback armchairs for a casual and cohesive display, then roll out a trellis rug to tie the area together with a pop of pattern. Dot nearby walls with a typographic decor and abstract canvas prints for an eye-catching display, then pair it with a beveled open mirror to open up space.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-martinique-tufted-sofa-lgly5819.html",
        "class_name": "Sofas",
        "sale_price": 869.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36990/38051686/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 72,
                "y": 31.09,
                "z": 33
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/106/1067862.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/89/897294.zip"
        }
    },
    {
        "sku": "LGLY5857",
        "product_name": "Craig Sofa",
        "product_description": "Lend a little dash of loft-worthy appeal and simply chic style to your aesthetic with this understated sofa, the perfect piece for any seating group or entertainment space. Featuring a clean-lined silhouette with rounded details and a gently tufted back, this sofa lends a bit of understated style and simply chic appeal to your ensemble, while the splayed legs lets you lean into a midcentury modern in subtle style. Add it to a seating group with a matching loveseat and arm chair to accommodate guests at your next neighborhood gathering, then add in glass-top tables and a geometric rug to tie it all together.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-craig-sofa-lgly5857.html",
        "class_name": "Sofas",
        "sale_price": 689.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/42462/39322594/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 80,
                "y": 32,
                "z": 32.5
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/107/1075945.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/90/905594.zip"
        }
    },
    {
        "sku": "LGLY6149",
        "product_name": "Lester Square Arms Sofa",
        "product_description": "Influenced by mid-century designs, this streamlined sofa sets a modern foundation in any seating group. Founded atop four slightly splayed conical legs in a warm brown finish, its frame is crafted from hardwood and padded with high-density foam to offer a medium-firm feel. 100% linen upholstery in a solid hue envelops the back, cushions, and track arms, giving this piece the versatility to blend with your existing arrangement, while square tufted details dot the back to enhance its clean-lined look. Some assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-lester-square-arms-sofa-lgly6149.html",
        "class_name": "Sofas",
        "sale_price": 599.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/37253/39596582/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 70.44,
                "y": 29,
                "z": 32.5
            },
            "glb": "http://img.wfrcdn.com/docresources/44316/107/1078698.glb",
            "obj": "http://img.wfrcdn.com/docresources/44316/97/971033.zip"
        }
    },
    {
        "sku": "LGLY6419",
        "product_name": "Alvarado Loveseat",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/langley-street-alvarado-loveseat-lgly6419.html",
        "class_name": "Sofas",
        "sale_price": 311.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/56500168/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 53.75,
                "y": 33.5,
                "z": 32.5
            },
            "glb": "http://img.wfrcdn.com/docresources/36991/119/1192002.glb",
            "obj": "http://img.wfrcdn.com/docresources/36991/121/1210111.zip"
        }
    },
    {
        "sku": "MTNA5155",
        "product_name": "Alijah Mid Century Vintage Modular Loveseat",
        "product_description": "This Mid Century Vintage Modular Loveseat adds a pop of color and style to your room. Designed to meet the demand of low cost but durable and efficient furniture, this compact sofa fits even smaller spaces while still providing plenty of room for two people to sit comfortably. You can put it anywhere in the house: living room, bedroom, study room, kids room or even hallway. The classic color design blends well with most of the home decor. This loveseat features extra thick seat and back cushion to enhance your comfort. No matter if you want to enjoy a cup of coffee during leisure time or have a business conversation in work days, this loveseat can be a great choice. A simple attitude towards lifestyle is reflected directly on the design, creating a trend of simple nature. Browse around this collection and you will find the furniture that fits your style and fits your budget.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mistana-alijah-mid-century-vintage-modular-loveseat-mtna5155.html",
        "class_name": "Sofas",
        "sale_price": 218.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/18669/41486174/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 44.97,
                "y": 28.03,
                "z": 26.88
            },
            "glb": "http://img.wfrcdn.com/docresources/44316/127/1274133.glb",
            "obj": "http://img.wfrcdn.com/docresources/44316/127/1279996.zip"
        }
    },
    {
        "sku": "MTNA8379",
        "product_name": "Mid Century Modern Sofa & Pillow Set",
        "product_description": "Bring a splash of midcentury-inspired style to your space with this chic sofa, a must-have anchor for any modern ensemble. Classic elements like grey upholstery and a brown and maple-finished wood frame come together with distinctive back tufts and flared legs to give this design its stylish streamlined look. Plus, it's topped with a pair of throw pillows detailed with elegant French script and postage details to tie together the look on arrival. While this sofa is perfect set atop a chic shag rug in the living room to glamorously gather friends at your next dinner party to enjoy tasty crudites and hand-crafted cocktails, its also a lovely den anchor for everyday relaxing. Try throwing a few woven throws over the back to cozy up for family movie night, or pull up an ottoman so you can effortlessly unwind with a cup of chamomile at the end of a long day.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/mistana-mid-century-modern-sofa-pillow-set-mtna8379.html",
        "class_name": "Sofas",
        "sale_price": 666.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/40128/38694870/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 85.87,
                "y": 33.05,
                "z": 35.55
            },
            "glb": "http://img.wfrcdn.com/docresources/40128/108/1088857.glb",
            "obj": "http://img.wfrcdn.com/docresources/40128/100/1002500.zip"
        }
    },
    {
        "sku": "ROSP2213",
        "product_name": "Colston Loveseat",
        "product_description": "Instantly elevate your well-appointed living room seating ensemble with an eye-catching accent with this wow-worthy wingback loveseat. Made with a solid rubberwood frame, this eye-catching design strikes a stunning high-back silhouette with dainty rolled arms and tapered square feet. Luxe black velvet upholstery with plush foam fill breathes new life into a traditional design, while glimmering faux crystal button tufting and gleaming chrome nailhead trim provide glamourous accents for upscale appeal. Establish a refined, glamourous aesthetic in your open concept living room by rolling out a soft damask area rug to define the space, then arrange this settee and a stately bergere armchair around a mirror-plated coffee table for a classic conversational ensemble. For a perfect finishing touch, install a glimmering beaded crystal chandelier overhead to wash the scene in dazzling light.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/rosdorf-park-colston-loveseat-rosp2213.html",
        "class_name": "Sofas",
        "sale_price": 566.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/47537039/1/furniture%2Fpdp%2Frosdorf-park-colston-loveseat.jpg",
        "model": {
            "dimensions_inches": {
                "x": 57.74,
                "y": 30.28,
                "z": 49.91
            },
            "glb": "http://img.wfrcdn.com/docresources/44319/108/1080732.glb",
            "obj": "http://img.wfrcdn.com/docresources/44319/98/985479.zip"
        }
    },
    {
        "sku": "THRE2400",
        "product_name": "Croydon Loveseat",
        "product_description": "Featuring rolled arms, bun feet, and a chocolate brown bonded leather upholstery, the Welborne Loveseat is a traditionally elegant addition to a living room or conversation space. Its distinctive features blend well with any classic setting, from traditional farmhouse to English County ranch. Bonded leather upholstery uses genuine leather fibers to ensure the look and feel of leather at an unparalleled price.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-croydon-loveseat-thre2400.html",
        "class_name": "Sofas",
        "sale_price": 399.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/30973/23310210/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 61,
                "y": 33.51,
                "z": 35.07
            },
            "glb": "http://img.wfrcdn.com/docresources/39354/109/1096732.glb",
            "obj": "http://img.wfrcdn.com/docresources/39354/105/1050650.zip"
        }
    },
    {
        "sku": "TRPT4018",
        "product_name": "Simmons Upholstery Hattiesburg Sterling Sofa",
        "product_description": "Anchor your seating group in approachable, transitional style with this versatile sofa. Founded atop tapered plastic feet, this clean-lined piece is made in the USA with a solid hardwood frame, sinuous spring supports, and foam and fiber fill to offer a medium seating firmness. Neutral gray linen upholstery envelops the design, allowing it to blend with any color palette you pick, while a cushion back and recessed arms round out the understated look. Five toss pillows are included for a decorative touch.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/three-posts-simmons-upholstery-hattiesburg-sterling-sofa-trpt4018.html",
        "class_name": "Sofas",
        "sale_price": 639.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/47136342/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 89.9,
                "y": 39,
                "z": 40.08
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/108/1080006.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/98/982700.zip"
        }
    },
    {
        "sku": "WADL4451",
        "product_name": "Spirit Lake Convertible Sleeper Sofa",
        "product_description": "Offering seating for three and an impromptu spot to snooze, this versatile convertible sleeper sofa features a fold-out design with a click-clack mechanism that makes it easy to host guests at a moment’s notice. Founded atop sleek cylindrical legs, this budget-friendly piece’s wooden frame is filled with foam and upholstered with solid-hued fabric. Its track arms and streamlined silhouette give it a contemporary, clean-lined look, while square tufted details dot the design for a touch of texture. Assembly is required.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/wade-logan-spirit-lake-convertible-sleeper-sofa-wadl4451.html",
        "class_name": "Sofas",
        "sale_price": 439.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/36989/40261377/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 86.43,
                "y": 34.12,
                "z": 31.85
            },
            "glb": "http://img.wfrcdn.com/docresources/36989/109/1091404.glb",
            "obj": "http://img.wfrcdn.com/docresources/36989/109/1091406.zip"
        }
    },
    {
        "sku": "WADL8173",
        "product_name": "Clarence Loveseat",
        "product_description": "Give your seating group a twist of today with this luxe loveseat. Simply center it against a blank wall in the den for a stylish start, then roll out a chic white shag rug on the floor below to anchor the ensemble. Founded atop four polished chrome-finished metal legs, this clean-lined design is wrapped in faux leather upholstery with a solid hue and gentle tufting along the seat back. Though it's certainly stunning sitting solo, you can lend a little extra allure by tossing on a pair of geometric-printed pillows.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/wade-logan-clarence-loveseat-wadl8173.html",
        "class_name": "Sofas",
        "sale_price": 349.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/36989/32851722/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 55.51,
                "y": 31.82,
                "z": 30.8
            },
            "glb": "http://img.wfrcdn.com/docresources/36989/128/1286454.glb",
            "obj": "http://img.wfrcdn.com/docresources/36989/129/1290746.zip"
        }
    },
    {
        "sku": "ZIPC2510",
        "product_name": "Sabine Sleeper Loveseat",
        "product_description": "Enjoy a contemporary modern look that adds comfort and style to your home with the Sabine convertible loveseat sleeper. European multi-functional style with a sleek design will inspire a fresh look and go perfectly in any room of the house.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-sabine-sleeper-loveseat-zipc2510.html",
        "class_name": "Sofas",
        "sale_price": 284.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/41606601/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 43.31,
                "y": 27.95,
                "z": 30.31
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/109/1099232.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/109/1099233.zip"
        }
    },
    {
        "sku": "ZIPC4022",
        "product_name": "Keanu Loveseat",
        "product_description": "Short on space? No problem! Here to help, this petite loveseat brings trendy looks home without stealing valuable real estate. Measuring 31.1'' H x 51.77'' W x 26.18'' D, this piece is a perfect fit for family rooms, offices, and like spaces. Faux leather upholstery gives this loveseat’s clean-lined design a touch of personality, while espresso-finished legs round out the look. Plus, the pair of back cushions removes, making general upkeep (and finding runaway TV remotes) less of a headache.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-keanu-loveseat-zipc4022.html",
        "class_name": "Sofas",
        "sale_price": 225.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/56827690/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 52.14,
                "y": 26.18,
                "z": 31.31
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/113/1132039.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/115/1155945.zip"
        }
    },
    {
        "sku": "ZPCD5744",
        "product_name": "Achilles Leather Sofa",
        "product_description": "This Sofa is perfect for a retro style home. Designed using elegance and comfort in mind, this sofa is constructed from premium-quality materials. Featuring a wooden frame, this sofa is strong and long lasting. This wooden sofa has square tapered wooden legs that ensure maximum stability for years to come. It is available in various colors, helping you choose the perfect one for your home without much hassle. Complete the beautiful sofa with the accent pillows for a wholesome look.",
        "product_page_url": "https://www.wayfair.com/furniture/pdp/zipcode-design-achilles-leather-sofa-zpcd5744.html",
        "class_name": "Sofas",
        "sale_price": 560.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/42219106/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 86,
                "y": 38,
                "z": 36
            },
            "glb": "http://img.wfrcdn.com/docresources/36987/108/1087105.glb",
            "obj": "http://img.wfrcdn.com/docresources/36987/98/988946.zip"
        }
    },
    {
        "sku": "ANDV2361",
        "product_name": "Melmore 25.75\" Table Lamp",
        "product_description": "Showcasing traditional styles through a contemporary lens, this 25.75” table lamp lends a touch of curated whimsy to your aesthetic. Made from resin in a dark oil rubbed bronze finish, this charming design showcases a scrollwork vine-shaped body on a raised round pedestal base, and sports an off-white tapered drum shade for an elegant contrast. Establish an inviting, transitional aesthetic in your open concept living room by setting a rich espresso-hued console table with straight square legs by a brightly-lit window dressed in vibrant chevron curtains and slubby linen sheers. Top the table with a row of travel books between two resin chess piece bookends and a sandalwood scented candle for an aromatic accent, then add this alluring lamp to illuminate the arrangement in a bright glow.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/andover-mills-melmore-2575-table-lamp-andv2361.html",
        "class_name": "Table Lamps",
        "sale_price": 52.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/45866104/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 12.5,
                "y": 12.5,
                "z": 25.73
            },
            "glb": "http://img.wfrcdn.com/docresources/30808/107/1078580.glb",
            "obj": "http://img.wfrcdn.com/docresources/30808/97/970359.zip"
        }
    },
    {
        "sku": "BL13362",
        "product_name": "Burton Table Lamp",
        "product_description": "More than just illumination for your abode, table lamps lend artful appeal to your space as they shine. Try adding one to your nightstand to give the master suite a mini makeover, or stage one atop the entryway console to greet guests with a warm glow. Take this one for example: charmingly lantern-like with its curved steal frame finished in chrome and featuring a hanging light highlighted by a cage shade.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/birch-lane-burton-table-lamp-bl13362.html",
        "class_name": "Table Lamps",
        "sale_price": 125.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/63010983/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 11.35,
                "y": 8.14,
                "z": 27.31
            },
            "glb": "http://img.wfrcdn.com/docresources/25006/131/1317097.glb",
            "obj": "http://img.wfrcdn.com/docresources/25006/132/1329006.zip"
        }
    },
    {
        "sku": "BL3138",
        "product_name": "Harding 2-Piece Lamp Set",
        "product_description": "Crafted of metal in a restored brass finish, this coordinating desk lamp and floor lamp exude timeless style. Sold as a set. ",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/birch-lane-harding-2-piece-lamp-set-bl3138.html",
        "class_name": "Table Lamps",
        "sale_price": 205.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/25006/10998054/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 40.79,
                "y": 21.39,
                "z": 59
            },
            "glb": "http://img.wfrcdn.com/docresources/25006/129/1293516.glb",
            "obj": "http://img.wfrcdn.com/docresources/25006/129/1296290.zip"
        }
    },
    {
        "sku": "BLK1709",
        "product_name": "Edison 18\" Table Lamp with Globe Shade",
        "product_description": "More than just illumination for your abode, table lamps lend artful appeal to your space as they shine. Try adding one to your nightstand to give the master suite a mini makeover, or stage one atop the entryway console to greet guests with a warm glow. Take this one for example: modeled after a lightbulb, it pairs a metal base with a rounded, clear glass shade for an industrial appearance.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/birch-lane-kids-edison-18-table-lamp-with-globe-shade-blk1709.html",
        "class_name": "Table Lamps",
        "sale_price": 67.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/63568071/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 11.53,
                "y": 11.53,
                "z": 18
            },
            "glb": "http://img.wfrcdn.com/docresources/2576/131/1313359.glb",
            "obj": "http://img.wfrcdn.com/docresources/2576/131/1315981.zip"
        }
    },
    {
        "sku": "EBDG2481",
        "product_name": "Bergh 17\" Desk Lamp",
        "product_description": "A no-brainer for dorm rooms and corner offices alike, this desk lamp lights up your work space in style. Standing 17'' tall, its brushed metal frame features an adjustable design that lets you get the glow right where you need it. A single light is highlighted by a plastic cone shade, directing the light and creating warm ambience. Plus, there's two electrical outlets on the base, so you never have to reach when your phone or laptop needs to be charged.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/ebern-designs-bergh-17-desk-lamp-ebdg2481.html",
        "class_name": "Table Lamps",
        "sale_price": 31.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/54698898/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 5.99,
                "y": 11.38,
                "z": 16.96
            },
            "glb": "http://img.wfrcdn.com/docresources/44308/112/1126448.glb",
            "obj": "http://img.wfrcdn.com/docresources/44308/114/1147958.zip"
        }
    },
    {
        "sku": "GOLV4188",
        "product_name": "Zoller Metal Adjustable 20\" Desk Lamp",
        "product_description": "Light up your work space or get the glow going in a cozy reading nook with this distinctive desk lamp, sure to add style as it shines. Its streamlined frame is crafted from metal and features a neutral gray finish, while a wood accent on top adds industrial contrast for a look that fits right into lofts and modern farmhouses alike. Measures 19.75'' H x 7'' W x 11.75'' D.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/george-oliver-zoller-metal-adjustable-20-desk-lamp-golv4188.html",
        "class_name": "Table Lamps",
        "sale_price": 81.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/60689979/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 7.1,
                "y": 15.65,
                "z": 20.81
            },
            "glb": "http://img.wfrcdn.com/docresources/44316/134/1346824.glb",
            "obj": "http://img.wfrcdn.com/docresources/44316/135/1354821.zip"
        }
    },
    {
        "sku": "IVBX2760",
        "product_name": "Bohl 22'' Desk Lamp",
        "product_description": "Illuminate your desk or bedside with this artful table lamp, showcasing an adjustable design and metal cone shades with contrasting interiors.   ",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/ivy-bronx-bohl-22-desk-lamp-ivbx2760.html",
        "class_name": "Table Lamps",
        "sale_price": 83.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/367/38145676/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 20.97,
                "y": 7.2,
                "z": 21.73
            },
            "glb": "http://img.wfrcdn.com/docresources/44318/116/1164316.glb",
            "obj": "http://img.wfrcdn.com/docresources/44318/117/1174641.zip"
        }
    },
    {
        "sku": "LFMF3250",
        "product_name": "Alejandro 26\" Desk Lamp",
        "product_description": "This 26\" Table Lamp features a dark brown finish and a linen fabric shade.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/alejandro-26-desk-lamp-lfmf3250.html",
        "class_name": "Table Lamps",
        "sale_price": 136.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/57195130/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 10,
                "y": 16.98,
                "z": 26.01
            },
            "glb": "http://img.wfrcdn.com/docresources/42526/120/1203138.glb",
            "obj": "http://img.wfrcdn.com/docresources/42526/121/1216930.zip"
        }
    },
    {
        "sku": "LGLY6964",
        "product_name": "Bella 26 Table Lamp",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/langley-street-bella-26-table-lamp-lgly6964.html",
        "class_name": "Table Lamps",
        "sale_price": 61.46,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/54477302/1/lighting%2Fpdp%2Flangley-street-bella-26-table-lamp.jpg",
        "model": {
            "dimensions_inches": {
                "x": 13.97,
                "y": 13.97,
                "z": 25.5
            },
            "glb": "http://img.wfrcdn.com/docresources/44325/116/1162825.glb",
            "obj": "http://img.wfrcdn.com/docresources/44325/117/1174403.zip"
        }
    },
    {
        "sku": "LRFY1999",
        "product_name": "Athenis 26.5\" Desk Lamp",
        "product_description": "Portable and stylish, lightweight with abundant illumination – what's not to love about table lamps? Perfect in any room that needs a bit more brightness that doubles as decor, lamps like this are great additions anywhere. A great touch for an industrial look, this piece features an black finish and an iridescent amber glass shade with a top-inspired silhouette. Crafted from steel, the slender hook shape and wide shade are sure to catch the eye. Accommodates a 60 W bulb, and we recommend an Edison bulb to complete the look. Measures 26.5'' H x 15.5'' W x 9.86'' D.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/athenis-265-desk-lamp-lrfy1999.html",
        "class_name": "Table Lamps",
        "sale_price": 86.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/58575396/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 15.5,
                "y": 9.59,
                "z": 26.49
            },
            "glb": "http://img.wfrcdn.com/docresources/42526/128/1284072.glb",
            "obj": "http://img.wfrcdn.com/docresources/42526/128/1289702.zip"
        }
    },
    {
        "sku": "MCRF3094",
        "product_name": "Borlon 21\" Desk Lamp",
        "product_description": "Illuminate your workspace or reading nook in elegant Art Deco style with this ultrachic 21\" desk lamp. Crafted of metal in an antique brushed brass finish, this dapper design features a straight, slender, tubular metal body a dramatically-curved neck, while a chunky square transparent acrylic base provides stylish support. A matching brass cone shade rounds out the design, directing bright light where it’s needed most. Powered by a 60\" cord, this fixture accommodates one 60 W LED bulb (not included).",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/mercer41-borlon-21-desk-lamp-mcrf3094.html",
        "class_name": "Table Lamps",
        "sale_price": 132.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/49421841/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 12.05,
                "y": 6.58,
                "z": 21.14
            },
            "glb": "http://img.wfrcdn.com/docresources/39355/108/1083761.glb",
            "obj": "http://img.wfrcdn.com/docresources/39355/104/1049119.zip"
        }
    },
    {
        "sku": "TRNT2776",
        "product_name": "Keystone Lantern 16\" Desk Lamp",
        "product_description": "A sophisticated take on an industrial design, this table lamp lends a touch of buttoned-up appeal to your aesthetic. Made from iron in a handsome matte black finish, this charming design showcases a tubular metal body, a chunky circle pedestal base, and an exposed finial bulb ensconced in a clean-cut cylindrical clear glass shade. Establish a curated aesthetic in your home office by rolling a channel-tufted leather task chair up to a reclaimed wood writing desk with chunky square legs. Top the desk with a pair of minimalist speakers, a charging station for your laptop, and a row of vintage novels between two wrought iron gear bookends, then add this alluring lamp to illuminate the late-night work sessions in a warm glow.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/trent-austin-design-keystone-lantern-16-desk-lamp-trnt2776.html",
        "class_name": "Table Lamps",
        "sale_price": 39.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/44661533/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 5.74,
                "y": 8.67,
                "z": 18.89
            },
            "glb": "http://img.wfrcdn.com/docresources/37312/107/1076951.glb",
            "obj": "http://img.wfrcdn.com/docresources/37312/93/931827.zip"
        }
    },
    {
        "sku": "TRPT1522",
        "product_name": "Hannon Swing Arm 29.5\" Desk Lamp",
        "product_description": "If you're stumped with how to style an end table, we've got all the alluring essentials to make your sofa-side stunning! Start with a personalized touch to make it all your own and set the tone - framed family photos are an easy addition, but you can always try a treasured travel souvenir or a homemade craft. Next, up the earthy elegance with a lush potted succulent. If you've really got a green thumb, splash your space with garden grace by adding on a vase of freshly-picked tulips. And finally, let it shine with this lovely lamp. Crafted of sleek metal, its base offers molded details and a swing arm. To top it all off, the glow of its single light is highlighted by a fabric empire shade.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/three-posts-hannon-swing-arm-295-desk-lamp-trpt1522.html",
        "class_name": "Table Lamps",
        "sale_price": 109.99,
        "thumbnail_image_url": "https://secure.img1.wfcdn.com/lf/43/hash/2664/42783671/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 16.28,
                "y": 18.55,
                "z": 29.47
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/109/1096788.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/102/1022969.zip"
        }
    },
    {
        "sku": "TRPT5424",
        "product_name": "Boulton Spiral Cage 24.5\" Table Lamp",
        "product_description": "Bring airy and understated contemporary style to any arrangement with this pair of 24.5\" table lamps, perfect for brightening bedside tables or flanking a decorative display in the foyer. Crafted of metal, their curved bases showcase an openwork design and a rubbed bronze finish for a versatile look that blends with a variety of color palettes and aesthetics. Cream-colored fabric shades (made from a blend of cotton, polyester, and linen) sit up above to diffuse the light from LED lightbulbs (included) in an ambient direction, while three-way switches right below the bulbs let you adjust the brightness.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/three-posts-boulton-spiral-cage-245-table-lamp-trpt5424.html",
        "class_name": "Table Lamps",
        "sale_price": 92.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/23460/37858844/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 13.6,
                "y": 13.59,
                "z": 24.79
            },
            "glb": "http://img.wfrcdn.com/docresources/30973/125/1258517.glb",
            "obj": "http://img.wfrcdn.com/docresources/30973/126/1263694.zip"
        }
    },
    {
        "sku": "UNRS3213",
        "product_name": "Domenica 18\" Table Lamp",
        "product_description": "Fun design elements dress up the traditional look of this Domenica 18\" Table Lamp. Crafted from iron, it offers a hint of earthly emphasis with wood joints. The combination works beautifully, adding a nature-inspired approach to your home office or kitchen decor.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/union-rustic-domenica-18-table-lamp-unrs3213.html",
        "class_name": "Table Lamps",
        "sale_price": 55.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/57993680/1/lighting%2Fpdp%2Funion-rustic-domenica-18-table-lamp.jpg",
        "model": {
            "dimensions_inches": {
                "x": 14.92,
                "y": 8.33,
                "z": 19.45
            },
            "glb": "http://img.wfrcdn.com/docresources/44278/128/1285768.glb",
            "obj": "http://img.wfrcdn.com/docresources/44278/129/1290540.zip"
        }
    },
    {
        "sku": "WLGN8250",
        "product_name": "Cremorne LED 28\" Desk Lamp",
        "product_description": "",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/wade-logan-cremorne-led-28-desk-lamp-wlgn8250.html",
        "class_name": "Table Lamps",
        "sale_price": 146.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/61822760/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 19.17,
                "y": 3.5,
                "z": 28.02
            },
            "glb": "http://img.wfrcdn.com/docresources/36989/119/1195712.glb",
            "obj": "http://img.wfrcdn.com/docresources/36989/121/1213052.zip"
        }
    },
    {
        "sku": "ZIPC8778",
        "product_name": "Zainab 17\" Desk Lamp",
        "product_description": "Fusing function with fashion, adjustable lamps lend industrial appeal to your ensemble while also allowing you to get the gleam right where you need it. Take this lamp for example: founded atop a circular base with space to corral office supplies, its frame is crafted from plastic and metal. The single light is highlighted by a bowl shade and sits on a twisting neck with a switch, so you can shine it right at the book you're reading or journal you're scrawling in.",
        "product_page_url": "https://www.wayfair.com/lighting/pdp/zipcode-design-zainab-17-desk-lamp-zipc8778.html",
        "class_name": "Table Lamps",
        "sale_price": 20.99,
        "thumbnail_image_url": "https://secure.img.wfcdn.com/lf/43/hash/2664/48273940/1/custom_image.jpg",
        "model": {
            "dimensions_inches": {
                "x": 8.87,
                "y": 6.83,
                "z": 17.5
            },
            "glb": "http://img.wfrcdn.com/docresources/30593/108/1081881.glb",
            "obj": "http://img.wfrcdn.com/docresources/30593/103/1037868.zip"
        }
    }
]
d=[]
for item in lis:
    d.append(item["product_name"].replace('"'," inches"))
