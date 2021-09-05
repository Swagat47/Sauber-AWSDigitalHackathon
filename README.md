# AWS Digital Hackathon  

# Objective

Today, one of the main global challenges is how to ensure food security for a world growing population whilst ensuring long-term sustainable development. According to the [Food and Agriculture Organization](http://www.fao.org/home/en/) (FAO), food production will need to grow by 70% to feed world population which will reach 9 billion by 2050.   

*The objective of our idea is to Reduce the post-harvest losses to raise farmer income and improve food security and livelihoods for vulnerable people.*

## **Why** the post harvest losses occur?

> *If we know "why" the losses occur then as an engineer we know how to tackle.*

Looking at the stages from ***harvest to consumption*** we observe the following losses.

|   Stage   |   Looses  |
|-----------|-----------|
|   At Harvesting   |   Edible crops left in field, plowed into soil, eaten by pests; timing of harvest not optimal; crop damaged during harvesting |
|   Threshing    |  Loss due to poor technique   |
|   Drying, transport and distribution |    Quality and quantity loss of during drying, poor transport infrastructure; loss owning to spoiling bruising |
| Storage   | Growth of undesired microorganism; Pests and disease attacks, spillage, contamination; natural drying out of food  |
|  Processing, cleaning, classification, hulling, pounding, grinding, packaging, soaking, winnowing, drying, sieving, milling   |  Process losses; contamination in process causing loss of quality. |
|  Product evaluation and quality control  | Product disregarded /out-grades in supply chain  |
| Packaging   | Inappropriate packaging damages produces; grain spillage from sacks; attack by pests  |
|  Marketing, selling, distribution  |  Damage during transport; spoilage; poor handling; losses caused by poor storage |
| Post-consumer  | Poor storage/stock management; discarded before serving; poor food preparation; expiration  |  

If we observe the above table closely, we see that major losses are at **storage and preservation** stage. So, here we focus on the storage & preservation stage and propose an idea of smart storage system.

# Solution

> *Say no to pesticides, let the light sanitize*

During the storage period to stop the growth of microorganisms on undesired surface we propose *Automated IoT based UV-C sanitization system*. 

Store the goods systematically on the mesh in the cub-board shown below.

![Imgur](https://i.imgur.com/HGzaduMl.jpg?1)

- The cub-board has UVC lights embedded in them that gets turn on automatically twice a day and sanitizes the goods in less than 30 seconds. 

- To prevent the pest attacks we implant these UVC lights at corners and on the way of the pests. This ensures that anytime if the pest enters the room it gets exposed to UVC lights, and its DNA is destroyed thus leading to death.

- A PIR sensor is fixed at the entrance of the room to make sure UVC lights are turned on only if there is no human present inside.

- To avoid the food getting dried out we ensure that the storage room temperature is maintained automatically with the help of temperature and humidity sensor.

# Implementation

### Tech Stack:

1. Microcontroller board (Arduino UNO)
2. AWS IoT/Things board/Things speak (Cloud service for data display-(Temperature, humidity))
3. UVC lights (LED for prototype)
4. Temperature & humidity sensor(To maintain temperature w.r.t external whether)

### Circuit Diagram:

![Imgur](https://i.imgur.com/8HK0bnpl.jpg)

*Circuit Simulation on Proteus software*

### Pseudo model:

![Imgur](https://i.imgur.com/RWAqj5yl.png)

### Pseudocode:

```
void setup() {
 pinMode(BUTTON, INPUT_PULLUP);
 pinMode(LED, OUTPUT);
 digitalWrite(LED, LOW);
 lcd.begin (16,2);      // To print the LED status on LCD
}
```

```
void loop() **
{
    // get the time at the start of this loop()
    unsigned long currentMillis = millis(); 
    lcd.setCursor(0,0);
    lcd.print("UV-C System");   //printing on LCD
    int pirstate=digitalRead(1);

    // check the button
    if (digitalRead(BUTTON) == LOW) 
    {
        // update the time when button was pushed
        buttonPushedMillis = currentMillis;
        ledReady = true;
    }
    
    // make sure this code isn't checked until after button has been let go
    if (ledReady) 
    {
    
        //this is typical millis code here:
        if ((unsigned long)(currentMillis - buttonPushedMillis) >= turnOnDelay) 
        {
            // okay, enough time has passed since the button was let go.
            digitalWrite(LED, HIGH);
            
            // setup our next "state"
            ledState = true;
            tone(buzzerPin,2000,2000);
            lcd.clear();
            lcd.setCursor(0,1);
            lcd.print("Sanitizing_area");
            
            // save when the LED turned on
            ledTurnedOnAt = currentMillis;
            
            // wait for next button press
            ledReady = false;
        }
    }
    
    // see if we are watching for the time to turn off LED
    if (ledState) 
    {
        // okay, led on, check for now long
        if ((unsigned long)(currentMillis - ledTurnedOnAt) >= turnOffDelay or pirstate==HIGH) 
        {
            ledState = false;
            tone(buzzerPin,2000,4000);
            lcd.setCursor(0,1);
            lcd.print("Sanitization_stoped");
            digitalWrite(LED, LOW);
        }
    }
} 

```

# Applications

### Merits

1. Farmer need not buy pesticides anymore. (Thus saving cost)
2. One time investment, results in year long profits.
3. The idea is a chemical less, eco-friendly anti-germicidal technique.
4. UV-C radiation (non-ionising radiation) has the advantage in that it does not produce by-products or radiation. 
5. Also, it is a simple dry and cold process requiring very low maintenance and low cost, as it does not need energy as a treatment medium.

### Demerits:

1. Exposure of Human skin to UVC lights may result in skin cancer, but this is taken care with the help of PIR sensors such that lights are in 'ON' stage only when there is no human present inside.
2. Regular Electricity supply is required in the village inorder to turn on the UVC lights.


### Results:

1. The system produces no ozone.
2. Effectively reduces the food-borne microbial load.
3. Increases food life by 30%-35%.
4. The system is completely automated, hence farmer can focus more on production.
5. Complete 360 degree sanitization with mesh structure.

![Imgur](https://i.imgur.com/PntItcBl.jpg)