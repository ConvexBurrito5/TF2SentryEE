## List of all the parts needed:
<details><summary>1) Linux based Laptop/PC</summary>
Brain of the Operation

- $0 - To help skew the final number im going to cheat and assume you are reading this on a PC. If not L33T and on linux already (Like me), look into dual booting.

Notes:
  - I ended up using an old lenovo Thinkpad that was tossed from work.
------
</details>

<details><summary>2) FT232H Adafruit chip</summary>
Used to convert USB -> GPIO/I2C

- $20: [Amazon](https://www.amazon.com/gp/product/B00XW2MD30/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

Notes:

- Purchase the official Adafruit FT232H. I could not get the off brand version to work.
------
</details>

<details><summary>3) Arduino Uno (QTY 2)</summary>
One handles I2C communication, the other handles the Wrangler.

- $14: [Amazon](https://www.amazon.com/ELEGOO-Board-ATmega328P-ATMEGA16U2-Compliant/dp/B01EWOE0UU/ref=sr_1_2?crid=1C659FL2TX65S&dib=eyJ2IjoiMSJ9.MazmhFfn-DF8W5oyX_S-tDFAqLRDaMJSkroaZhdQMdgMaQkGbBimooKwa4LhivNhcV__Luad1q2S8ABMsOf55C3M63jmVrQQEawwazcT8qEqQTKpC1AMHdFlkMnPxR6MAWZg05gedii8B6Ym-gH-vfGlsupm0Q87rvMq2n8f_9v9ah8vPDlgNRTgjuL12mWAaP4GLnAS4lS0psSqiKqu5is_qhd4SAd4LBMDGZ0ooBsWw3hwuEcG_tD0GlGLCybCKFR2rz9X8bZsScF0HiYn3a4kk5S152GbUMDWcaX5ygk.ameo07XYVm9n_OgyGW5WkO880bLArDBQoSkR8xDOiek&dib_tag=se&keywords=arduino+uno&qid=1722721253&s=industrial&sprefix=aurduino+Uno%2Cindustrial%2C823&sr=1-2)
- $0.90 + $3 shipping: [AliExpress](https://www.aliexpress.us/item/3256802811531752.html?spm=a2g0o.productlist.main.7.4b87zrXRzrXRNd&algo_pvid=1e4532d7-986b-4535-b24c-55f9242018f1&aem_p4p_detail=202408031441427928841146003550005479432&algo_exp_id=1e4532d7-986b-4535-b24c-55f9242018f1-3&pdp_npi=4%40dis%21USD%213.18%210.99%21%21%213.18%210.99%21%402103243417227213022943527e753e%2112000023136335082%21sea%21US%210%21ABX&curPageLogUid=NBJdLLd8K0UG&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202408031441427928841146003550005479432_1)
------
</details>

<details><summary>4) 4 Relay Module (12V)</summary>
Used for Control of Airsoft gun, Laser pointer and the Hardware switch.

- $9: [Amazon](https://www.amazon.com/AEDIKO-Channel-Optocoupler-Isolation-Trigger/dp/B098DXRTT8/ref=sr_1_1?crid=A2WMXHRUJN50&dib=eyJ2IjoiMSJ9.GtoHaO1ozc2h-R7o5xzyY_WD6pM0EVNtylBAk1_fRn0afobC3TOaU1fqe74d2LLS_6TyG4dg3JwN-Mc9v030mBO9F-H7WwThG3Q2s9oVg39Odv7gP4kkp4p1ruVucaQNB9bcE5sQLnoTiAcgWN9bcR8k7vdqUdg4HMGgxpqdIWy2oQKyWlCqsBSfYSUKPE_GdMnXKc1Q1Gq4eo1uOZVpmHqHCwusIQeBFSGJWDgzGZdXEHY8NHd0IQS3BDqrSaZTJydL0IPYq3Dvd1MtVQTCjbS4gkezIU8-1r3a89UnCjg.1x4nryRUsqKKS5_WrJFlVyXqAFJAPshReK5hC2nQB48&dib_tag=se&keywords=4+relay+module+12v&qid=1722722967&s=industrial&sprefix=4+relay+module+12%2Cindustrial%2C291&sr=1-1) (Qty: 2)
- $1 + $3 Shipping: [AliExpress](https://www.aliexpress.us/item/3256802681413225.html?spm=a2g0o.productlist.main.1.51423b4clmKPD4&algo_pvid=2ec79dc5-f325-4cca-ab2f-6616719f07f1&algo_exp_id=2ec79dc5-f325-4cca-ab2f-6616719f07f1-0&pdp_npi=4%40dis%21USD%211.45%210.99%21%21%211.45%210.99%21%402103011617227230322434557e8210%2112000022927395897%21sea%21US%210%21ABX&curPageLogUid=3ZqIi0ihnlhK&utparam-url=scene%3Asearch%7Cquery_from%3A)
------
</details>

<details><summary>5) PCA9685 motor driver module</summary>
Used for I2C -> PWM to ctrl Servos

- $9: [Amazon](https://www.amazon.com/HiLetgo-PCA9685-Channel-12-Bit-Arduino/dp/B01D1D0CX2/ref=sr_1_2?crid=11W1SGQ8DBP7A&dib=eyJ2IjoiMSJ9.Vferr79XpoL6Bnem-ZY9xxuw-jR7G9gDmaht6SENJ2MPhJHPETOphZpcT6tiBrZw4T68W1BhdtlnoOpXmJRf0jay62PHUsDlGef7YPL9mYAGeSeuwPG1ct49k-bpBE20Ss68Wg8RI3bZxtsciD-iZrvQ7SIrjlB8the5NKcdXZSp2AbQb-fHIMg0LbXKb1qQWKSxUIh8PGVXFZNjIXd2T2xryrSm9wo5cFXk2sQLODdYCaFe_8QGCTgFsgk4YSVO2yAe0OVJoyHPOB7frvi-c1L9XhyruuaMrkT9_HHr8_g.Hi1EFaNHJCx-DjutLi4VyG6MomIKZZlSF6cy1dIh-C8&dib_tag=se&keywords=pca9685&qid=1722723221&s=industrial&sprefix=pca9685+%2Cindustrial%2C277&sr=1-2) (Qty: 1)
- $2.3: [Aliexpress](https://www.aliexpress.us/item/3256804772762018.html?spm=a2g0o.productlist.main.1.7aa461f04mQYG0&algo_pvid=954cff13-0ac5-44c7-9ce6-7fda4c647b28&algo_exp_id=954cff13-0ac5-44c7-9ce6-7fda4c647b28-0&pdp_npi=4%40dis%21USD%212.32%210.99%21%21%212.32%210.99%21%402101fb1917227231323886430e84b0%2112000031156876977%21sea%21US%210%21ABX&curPageLogUid=OdHdYyz2EC5x&utparam-url=scene%3Asearch%7Cquery_from%3A)
------
</details>

<details><summary>6) Y Servo (3 Wire, 20KG Servo Motor)</summary>
Used for the Y axis rotation

- $16: [Amazon](https://www.amazon.com/Torque-Motors-Waterproof-Steering-Control/dp/B073F92G2S/ref=sr_1_5?crid=1I7J7JHGWH6LC&dib=eyJ2IjoiMSJ9.usDUirxtaJa3ZG3ozfBB-l39FpOhq3ZliP9gny8dYRbyJhgSp8Buu1jz5cF2Vo4IqWDSx5tRdWP_0XtfqVVtBkhIdJswmFT3qs5CRgxVjaWMrwcbx7RLfiVjD0CPgXgJb4HafteDlNbXb4yp5-rHLKd6ssXM53RquaeQy-8pjdPE6Ked-GRi5a98R0EUtSH3LKTovysqIjk6bMChS6aaYw_o53l0Aun3oy3RlPgkO3Xd5mn5IjoHcNYxSyd1WrOzsublcm5ZgsRpEc1ALTBJAJtv2NNDlbAQfCq_PJvZwVs.l6B_jmq4ZUnvDjQ7yCX6STgAp4IKsv8CFTOHi3gDJyQ&dib_tag=se&keywords=20+kg+270deg+servo&qid=1722723402&sprefix=20+kg+270deg+serv%2Caps%2C280&sr=8-5)

Notes:

- I strongly suggest you copy the servos I have chosen. Makes life 100% easier when building.
- Full disclosure, servo torque is arbitrary. I guessed... May be overkill.
------
</details>

<details><summary>7) X Servo (3 Wire, 35KG Servo Motor)</summary>
Used for X axis rotation

- $29: [Amazon](https://www.amazon.com/gp/product/B09F9DGN57/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

Notes:

- I strongly suggest you copy the servos I have chosen. Makes life 100% easier when building.
- Full disclosure, servo torque is arbitrary. I guessed... May be overkill.
------
</details>


--------------------
8) USB Laser pointer (1)
    - Cheapest laser pointer that has USB charging.
    - $10: Amazon (1)
9) Airsoft gun (1)
    - Any airsoft gun works however, if you pick an 'AEG' (Electric) the theory behind the firing mechanism will still work.
    - I used "Lancer Tactical Gen 2 LT-19 airsoft M4 Carbine 10" because its what I had lying around. Documentation and CAD files match this.
    - $189: Amazon (1)
10) 12V Battery (A ___AH is required for 4 hours of on-time) (1)
    - I currently am using a 10AH battery.
    - Load calculations will determine the final size of the battery.
    - $40: Amazon (1)
11) 12V -> 7.6V DC-DC Buck converter (1)
    - Used to step from 12 -> 7.6 for Servos
    - I used Amazons Generic: 'DC-DC Buck Converter 3.5-30V to 0.8-29V 10A....'
    - $13: Amazon (1)
12) 12V DC jack 2.1mm ID/ 5.5mm OD (2)
    - Used to power Arduino
    - $7: Amazon (5)
13) Rocker Switch 0N/OFF (1)
    - Used as Hardware safety for airsoft gun and servos
    - $8: Amazon (10)
14) NRF24L01+ Wireless Transceiver Module (1)
    - Radio communication between wrangler/turrent
    - $8: Amazon (4)
15) 3D Printer Filament
    - For turret 10KG of fillament, 
    - For wrangler 1KG of fillament,
    - I purchased bulk PLA fillament from AliExpress 10KG for 83$.
    - If Purchased off Amazon: $13 e/a
    - AliExpress:
      - Turret: $83
      - Wrangler: $9
    - Amazon:
      - Turrent: $130
      - Wrangler: $13
16) 4 Position Joystick (1)
    - Used to control wrangler
    - $15: Amazon (1)
17) Momentary Push button (1)
    - Used for Firing Wrangler
    - $11: Amazon (24)
18) USB camera (1)
    - Used for image detection
    - $20: Amazon(1)
19) Assorted items
    - Wire
      - 14,16,18 and regular breadboard wires were used.
      - I used higher quality 18 gauge solid copper wires for logic wires to help keep organized.
    - Dupont connections (OPT)
      - I used this sometimes to terminate my 18 gauge wire when it was being used...
    - Solder + Iron
    - Assorted circuitry components...
      - (2) 10uF Capacitors
      - (1) 10K Resistor
    - 9v Battery to power Wrangler Arduino

## Total:
Price Depends on where you purchase from:
- Amazon:
    - $576 
- Amazon/AliExpress:
    - $498

This price is quite steep. A major price cut could be made by choosing a different Airsoft gun, $189 price is steep.

I have had most pieces lying around. I spent maybe 300$ to get this all going.