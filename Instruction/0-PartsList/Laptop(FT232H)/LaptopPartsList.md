## List of all the parts needed:
<details><summary>1) Linux based Laptop/PC</summary>

-----
 Brain of the Operation

- $0 - To help skew the final number im going to cheat and assume you are reading this on a PC. If not L33T and on linux already (Like me), look into dual booting.

Notes:
  - I ended up using an old lenovo Thinkpad that was tossed from work.
------
</details>

<details><summary>2) FT232H Adafruit chip</summary>

-----
Used to convert USB -> GPIO/I2C

- $20: [Amazon](https://www.amazon.com/gp/product/B00XW2MD30/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

Notes:

- Purchase the official Adafruit FT232H. I could not get the off brand version to work.
------
</details>

<details><summary>3) Arduino Uno (QTY 2)</summary>

-----
One handles I2C communication, the other handles the Wrangler.

- $14: [Amazon](https://www.amazon.com/ELEGOO-Board-ATmega328P-ATMEGA16U2-Compliant/dp/B01EWOE0UU/ref=sr_1_2?crid=1C659FL2TX65S&dib=eyJ2IjoiMSJ9.MazmhFfn-DF8W5oyX_S-tDFAqLRDaMJSkroaZhdQMdgMaQkGbBimooKwa4LhivNhcV__Luad1q2S8ABMsOf55C3M63jmVrQQEawwazcT8qEqQTKpC1AMHdFlkMnPxR6MAWZg05gedii8B6Ym-gH-vfGlsupm0Q87rvMq2n8f_9v9ah8vPDlgNRTgjuL12mWAaP4GLnAS4lS0psSqiKqu5is_qhd4SAd4LBMDGZ0ooBsWw3hwuEcG_tD0GlGLCybCKFR2rz9X8bZsScF0HiYn3a4kk5S152GbUMDWcaX5ygk.ameo07XYVm9n_OgyGW5WkO880bLArDBQoSkR8xDOiek&dib_tag=se&keywords=arduino+uno&qid=1722721253&s=industrial&sprefix=aurduino+Uno%2Cindustrial%2C823&sr=1-2)
- $0.90 + $3 shipping: [AliExpress](https://www.aliexpress.us/item/3256802811531752.html?spm=a2g0o.productlist.main.7.4b87zrXRzrXRNd&algo_pvid=1e4532d7-986b-4535-b24c-55f9242018f1&aem_p4p_detail=202408031441427928841146003550005479432&algo_exp_id=1e4532d7-986b-4535-b24c-55f9242018f1-3&pdp_npi=4%40dis%21USD%213.18%210.99%21%21%213.18%210.99%21%402103243417227213022943527e753e%2112000023136335082%21sea%21US%210%21ABX&curPageLogUid=NBJdLLd8K0UG&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202408031441427928841146003550005479432_1)
------
</details>

<details><summary>4) 4 Relay Module (12V)</summary>

-----
Used for Control of Airsoft gun, Laser pointer and the Hardware switch.

- $9: [Amazon](https://www.amazon.com/AEDIKO-Channel-Optocoupler-Isolation-Trigger/dp/B098DXRTT8/ref=sr_1_1?crid=A2WMXHRUJN50&dib=eyJ2IjoiMSJ9.GtoHaO1ozc2h-R7o5xzyY_WD6pM0EVNtylBAk1_fRn0afobC3TOaU1fqe74d2LLS_6TyG4dg3JwN-Mc9v030mBO9F-H7WwThG3Q2s9oVg39Odv7gP4kkp4p1ruVucaQNB9bcE5sQLnoTiAcgWN9bcR8k7vdqUdg4HMGgxpqdIWy2oQKyWlCqsBSfYSUKPE_GdMnXKc1Q1Gq4eo1uOZVpmHqHCwusIQeBFSGJWDgzGZdXEHY8NHd0IQS3BDqrSaZTJydL0IPYq3Dvd1MtVQTCjbS4gkezIU8-1r3a89UnCjg.1x4nryRUsqKKS5_WrJFlVyXqAFJAPshReK5hC2nQB48&dib_tag=se&keywords=4+relay+module+12v&qid=1722722967&s=industrial&sprefix=4+relay+module+12%2Cindustrial%2C291&sr=1-1) (Qty: 2)
- $1 + $3 Shipping: [AliExpress](https://www.aliexpress.us/item/3256802681413225.html?spm=a2g0o.productlist.main.1.51423b4clmKPD4&algo_pvid=2ec79dc5-f325-4cca-ab2f-6616719f07f1&algo_exp_id=2ec79dc5-f325-4cca-ab2f-6616719f07f1-0&pdp_npi=4%40dis%21USD%211.45%210.99%21%21%211.45%210.99%21%402103011617227230322434557e8210%2112000022927395897%21sea%21US%210%21ABX&curPageLogUid=3ZqIi0ihnlhK&utparam-url=scene%3Asearch%7Cquery_from%3A)
------
</details>

<details><summary>5) PCA9685 motor driver module</summary>

-----
Used for I2C -> PWM to ctrl Servos

- $9: [Amazon](https://www.amazon.com/HiLetgo-PCA9685-Channel-12-Bit-Arduino/dp/B01D1D0CX2/ref=sr_1_2?crid=11W1SGQ8DBP7A&dib=eyJ2IjoiMSJ9.Vferr79XpoL6Bnem-ZY9xxuw-jR7G9gDmaht6SENJ2MPhJHPETOphZpcT6tiBrZw4T68W1BhdtlnoOpXmJRf0jay62PHUsDlGef7YPL9mYAGeSeuwPG1ct49k-bpBE20Ss68Wg8RI3bZxtsciD-iZrvQ7SIrjlB8the5NKcdXZSp2AbQb-fHIMg0LbXKb1qQWKSxUIh8PGVXFZNjIXd2T2xryrSm9wo5cFXk2sQLODdYCaFe_8QGCTgFsgk4YSVO2yAe0OVJoyHPOB7frvi-c1L9XhyruuaMrkT9_HHr8_g.Hi1EFaNHJCx-DjutLi4VyG6MomIKZZlSF6cy1dIh-C8&dib_tag=se&keywords=pca9685&qid=1722723221&s=industrial&sprefix=pca9685+%2Cindustrial%2C277&sr=1-2) (Qty: 1)
- $2.3: [Aliexpress](https://www.aliexpress.us/item/3256804772762018.html?spm=a2g0o.productlist.main.1.7aa461f04mQYG0&algo_pvid=954cff13-0ac5-44c7-9ce6-7fda4c647b28&algo_exp_id=954cff13-0ac5-44c7-9ce6-7fda4c647b28-0&pdp_npi=4%40dis%21USD%212.32%210.99%21%21%212.32%210.99%21%402101fb1917227231323886430e84b0%2112000031156876977%21sea%21US%210%21ABX&curPageLogUid=OdHdYyz2EC5x&utparam-url=scene%3Asearch%7Cquery_from%3A)
------
</details>

<details><summary>6) Y Servo (3 Wire, 20KG Servo Motor)</summary>

-----
Used for the Y axis rotation

- $16: [Amazon](https://www.amazon.com/Torque-Motors-Waterproof-Steering-Control/dp/B073F92G2S/ref=sr_1_5?crid=1I7J7JHGWH6LC&dib=eyJ2IjoiMSJ9.usDUirxtaJa3ZG3ozfBB-l39FpOhq3ZliP9gny8dYRbyJhgSp8Buu1jz5cF2Vo4IqWDSx5tRdWP_0XtfqVVtBkhIdJswmFT3qs5CRgxVjaWMrwcbx7RLfiVjD0CPgXgJb4HafteDlNbXb4yp5-rHLKd6ssXM53RquaeQy-8pjdPE6Ked-GRi5a98R0EUtSH3LKTovysqIjk6bMChS6aaYw_o53l0Aun3oy3RlPgkO3Xd5mn5IjoHcNYxSyd1WrOzsublcm5ZgsRpEc1ALTBJAJtv2NNDlbAQfCq_PJvZwVs.l6B_jmq4ZUnvDjQ7yCX6STgAp4IKsv8CFTOHi3gDJyQ&dib_tag=se&keywords=20+kg+270deg+servo&qid=1722723402&sprefix=20+kg+270deg+serv%2Caps%2C280&sr=8-5)

Notes:

- I strongly suggest you copy the servos I have chosen. Makes life 100% easier when building.
- Full disclosure, servo torque is arbitrary. I guessed... May be overkill.
------
</details>

<details><summary>7) X Servo (3 Wire, 35KG Servo Motor)</summary>

-----
Used for X axis rotation

- $29: [Amazon](https://www.amazon.com/gp/product/B09F9DGN57/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

Notes:

- I strongly suggest you copy the servos I have chosen. Makes life 100% easier when building.
- Full disclosure, servo torque is arbitrary. I guessed... May be overkill.
------
</details>

<details><summary>8) USB Laser pointer</summary>

------
Used to show the user where the turret is pointing when Wrangler mode is active.

- $10: [Amazon](https://www.amazon.com/Pointer-Indoor-Mouse-Interactive-Kitten/dp/B09TFNQM7Z/ref=sr_1_13?crid=FKO2KN0P414G&dib=eyJ2IjoiMSJ9.jghXMK1-qrrmFeHgZVNSEftWx2anowaCGTQU84QtLVy_iWvkdv_EOAqHHbs8KVBjyBz0Ugctva59v3s9IcifsO6v8pQu2jKEO2Mbnz67sIN1Z9D-eBZuRWQqAt8RLA1NxbLAcYD5LFJt60-Q__CUelPEwBbIGlCegpt1cxA7gNzhr6L8GgYvOHNjhdClMpSRUyUAhMGY91VM2UKJ6TiJCVAqCGnuahCA5vX46W-rWVi-xt6jFohZ1UvU4MVo29gDSz1KB3LYYo65bjVXreVy5KhS9iIyXUp4psW9JRu8Gs8.sYRUSg09Vgm5gTkCTu4GDzgpJYERrFsQHOupg-7BIFA&dib_tag=se&keywords=laser+pointer&qid=1722905100&sprefix=laser+pointe%2Caps%2C101&sr=8-13)

Notes:

- Cheapest laser pointer that has USB charging.
------
</details>

<details><summary>9) Airsoft gun</summary>

-----
Used for firing
- $189: [Amazon](https://www.amazon.com/gp/product/B07PZR76QS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

Notes:

- If you don't pick an 'AEG' (Electric) type Airsoft gun you will have to re-design the firing mechanism.
- I used "Lancer Tactical Gen 2 LT-19 Airsoft M4 Carbine 10" because it's what I had lying around. Documentation and CAD files match this.
------
</details>

<details><summary>10) 12V Battery (A ___AH is required for 4 hours of on-time)</summary>

------
Used to power everything
- $19: [Amazon](https://www.amazon.com/EXP1250-Terminals-Chamberlain-LiftMaster-Replacement/dp/B0010Z4MDK/ref=sr_1_6?crid=IKW56ODWN9O6&dib=eyJ2IjoiMSJ9.X8csgQtFQoACxgT9yTB45Z5_XNgff2P3aeaAebGcw8wM9eYwNXzvHxOqGr5f7qgEWN5j0V--Tx-22LvJnpfq6IW5tGenkSzTH2QO8jw2KspvXOIL1IwigeWLwt3njQDCSFYq8duSXYZ_oosRNBz4GCP-Lpvbth5G0tVgQ5zTR9O0SBnuKIDJ3KmTq2WFoMjjTKHqB_EveXhtBb39qiJ0alJPBefVJZuIYIyJFStjuf3uQ41mH6hn7BDE47XM2TUfa-MlhtzFkPpsZM3kBP318EXz_HiGR-okekba1E2OkXo.db-gqGKmUTkHCc0AqQfQ-tO8svwBwzzNj4eBSUEljTs&dib_tag=se&keywords=12v+5ah+battery&qid=1722915863&sprefix=12v+5ah+battery%2Caps%2C105&sr=8-6) 

Notes:
- I currently am using a 5AH battery.
- Load calculations will determine the final size of the battery.
------
</details>

<details><summary>11) 12V -> 7.6V DC-DC Buck converter</summary>

------
Used to step from 12 -> 7.6 for Servos
- $13: [Amazon](https://www.amazon.com/dp/B017SLMVXM?ref=nb_sb_ss_w_as-reorder_k0_1_14&amp=&crid=58HLQBY3IHZU&amp=&sprefix=buck+converter)

------
</details>

<details><summary>12) 12V DC jack 2.1mm ID/ 5.5mm OD</summary>

------
Used to power Arduino
- $6: [Amazon](https://www.amazon.com/Powerhugs-Supply-Repair-Barrel-Connector/dp/B0CRHBLCXD/ref=sr_1_20?crid=290VEE2HBCCEA&dib=eyJ2IjoiMSJ9.E-ycG5KbTQoNKluCaJEB9au2NLPp2WWi9H-NIGB9HXdJuv6b6Yw3DSa75CnkYD8H923F0pqz_Qor7VG-ff4_eXJHnq6BxX1G0bWIUZCW7xAddSNx2uMNvfvNVacVIOgkinbOn9WuGAMpDCHSXGFfyPTU8t7SKlQ75mZHtQ4085MDIo5j-yk6rmCmG23hKLKA.B5k70jexhT_UOiLRFqHozg3IgUovksV1nGXoeZf5W6o&dib_tag=se&keywords=12V+DC+jack+2.1mm+ID%2F+5.5mm+OD+male&qid=1722917104&sprefix=12v+dc+jack+2.1mm+id%2F+5.5mm+od+ma%2Caps%2C191&sr=8-20)

------
</details>

<details><summary>13) Rocker Switch 0N/OFF (QTY: 2)</summary>

------
Used as Hardware safety for airsoft gun and servos
Also used to toggle Wrangler

- $9: [Amazon](https://www.amazon.com/gp/product/B07XD8J2PL/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1)
------
</details>

<details><summary>14) NRF24L01+ Wireless Transceiver Module (QTY: 2)</summary>

------
Used for Radio communication between wrangler/turrent
- $8: [Amazon](https://www.amazon.com/gp/product/B00LX47OCY/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

------
</details>

<details><summary>15) 3D Printer Filament (PLA, 11KG)</summary>

------
Used to print the body for the Turrent/Wrangler
- $13: [Amazon](https://www.amazon.com/ANYCUBIC-Printer-Filament-Dimensional-Accuracy/dp/B0834W5L3L/ref=sr_1_1?dib=eyJ2IjoiMSJ9.mlB-HzqZw3F9azAJQCkbhQ0OSgwHfyRjTEj249lysVcGJkixNbBCSAsWl9_8yzPTxSmV2eJIwRouyjNZDq01UsAYUlz1qkd33C8OAVuj8FcGt3UZwFLoVbpp38M6l4lG5Wt2tnttoSmW611W8qZZ0V-k9LpYn0C-_SvU8kqQ8QLvxCDMW1JdHP9i4udkjzpZlSXrKPN0vl7Jpg1brKaIKLoKGF2-dKdeXTrVT87GfRQ.ICJU-JGRkNijU2coqfoglBuScYzLTkf2jKC0js65SO4&dib_tag=se&keywords=PLA+1kg&qid=1722917407&sr=8-1) (QTY: 1KG)
- 60-80$: [AliExpress](https://www.aliexpress.us/item/3256805838190590.html?spm=a2g0o.productlist.main.13.1cf071a0NIW9Y6&algo_pvid=39cb41b4-c538-4cfe-9e9b-f92240cbed00&algo_exp_id=39cb41b4-c538-4cfe-9e9b-f92240cbed00-6&pdp_npi=4%40dis%21USD%21205.19%2179.44%21%21%21205.19%2179.44%21%402101e81117229174547568918e570c%2112000035371468070%21sea%21US%214045313739%21X&curPageLogUid=ae4h60fcWOwy&utparam-url=scene%3Asearch%7Cquery_from%3A) (QTY: 10KG)

Notes:
- For turret 10KG of fillament, 
- For wrangler 1KG of fillament,
------
</details>

<details><summary>16) 4 Position Joystick</summary>

------
Used to control wrangler
- $15: [Amazon](https://www.amazon.com/CS-402-Momentary-Joystick-Position-Monolever/dp/B07D9JC75F/ref=sr_1_2?crid=18I9DQIFDXB79&dib=eyJ2IjoiMSJ9.JPsr_K9JyulYB9Oc-QOz1K_hRduKW98-nHeowcfW0KYWeR-di-L7hI2G_qlM4Oa7VLO_O710FiaeHaAPQQiVZPWWaYVNC1gauuNy5yw6k_vQJS1WiTlzMinlUNlD4B_9KiEKY0MXowNlWBaLcn51YochvvHTH-hfpoQ97ivdD100IshgzbirOh923Zi5-PBSZE9jhPEnY1vcwQELSiHkSULguvYHmC95aBHeiy9n5ao.Cdd1K-2oXtjv0Jypwrc0hexSUlKVd7hTJxbVnLbHflo&dib_tag=se&keywords=4+position+joystick&qid=1722917548&sprefix=4+position+joystic%2Caps%2C131&sr=8-2)
------
</details>

<details><summary>17) Momentary Push button</summary>

------
Used for Firing Wrangler
- $13: [Amazon](https://www.amazon.com/Momentary-pre-Wiring-Waterproof-Stainless-Normally/dp/B09BKWMNJ9/ref=sr_1_2?crid=32WHKUBI796YQ&dib=eyJ2IjoiMSJ9.V5zi0KXZD9IwpZrr7mc5yqlNI_gKMyPVh7ox6gZE8lCsJOiPvxXxA35aHXpSsF4N_STei9M0_l7HXkkw2Lw7BVZI0FtD8hWJlYhPxaKlflisn5a9eoq34_aym5oD22BzRNRzPdycX7YZKMJYpYG4nlmimz_Ofgyudic6hDJfFFCbxYkN2J_W9C0NhlAPqmRH9yU8bYtaeoESkqHKuLPVKUq448DvoX1aYvshtazmsdo.ZAeByzwWSEacCJOFKfCMPQManrsbAOofV5_-QOvZNIQ&dib_tag=se&keywords=momentary+push+button&qid=1722917593&sprefix=mometary+push+button%2Caps%2C114&sr=8-2)
------
</details>

<details><summary>18) USB camera</summary>

------
Used for image detection
- $20: [Amazon](https://www.amazon.com/Argmao-Microphone-110-degree-Streaming-Conferencing/dp/B09JZL2XX4/ref=sr_1_5?crid=IMAQWCAPDR67&dib=eyJ2IjoiMSJ9._ruWIhWb4hQzF4R9pd5XLn5fCW23_KUgDOz7Up7xvwgsckWrJIt65NmkJnOxC9GS5bEuMywj5lbRbHZPjernOo8lCuIg9G5BH-HVClkBSrYpRMxFLwRkygufp_x5Juw7ovP6DB44Daj2Yc0qZCyIGSum0i6P4oKwOwobicHvGeQfG3nYmpzS2DQafi9Pglxj968JOTVuCMvc_oDozA1jMv_6OV6kEqZsE0jwyh-JEuM.7fcxhw_3_A5mkOL3GR3p27aUXWR08T4b6EUhMkekhEw&dib_tag=se&keywords=usb+camera&qid=1722917639&sprefix=usb+camera%2Caps%2C105&sr=8-5)
------
</details>

<details><summary>19) 10uF Capacitor (QTY: 2)</summary>

------
Used to regulate the NRF24L01+ to prevent power fluctuations.
- $10: [Amazon](https://www.amazon.com/ALLECIN-Electrolytic-Capacitor-Assortment-Kit/dp/B0C1VBXCQM/ref=sr_1_1?crid=3ESKO0RC5CKNJ&dib=eyJ2IjoiMSJ9.ekYH7jx2EeGYfnpDMkTUbA5_8nAZM5NXRF7ISTCDYRfZ-VsUzH1Rc_HS1zH4QoIwZuOVG3gH71mNmdV9sSS3Jn9rKnkFlc9cxlQZWIqgtdYZcTq1U6iY1-vYTtu3aMd-_zLv-iI0EQlEsDvgiEFvp9gyq6OT5Ja1bdkJ2sU5XQ7CUhSfWOjsKIzW9ZlU7bZPPdYUns-DiSR8309QaKkkT6axEjl4stAr87-tpISMJEM.afn5f6xA9ckLaIJShDXEJfC9TrZQCFHFRFhiFwc8m3U&dib_tag=se&keywords=capacitor+kit&qid=1722917746&sprefix=capacitor+kit%2Caps%2C101&sr=8-1)
------
</details>

<details><summary>20) 10K Resistor</summary>

------
Used to for the wrangler 'on' signal LED.
- $10: [Amazon](https://www.amazon.com/BOJACK-Values-Resistor-Resistors-Assortment/dp/B08FD1XVL6/ref=sr_1_3?crid=2DSQ1JAM0TS15&dib=eyJ2IjoiMSJ9.8EDLQctdt9NzqYQqREI7yuKyO9o1cCE8nMUVCyQyUul-3sZkb3PzW74IjbL2BQHZXiHAbgFmB8KC01Ff_ei6OORJ4hmbZPd1M48m3s0DYJ1zx6lKVaC-QFBLTJpLfuFG1sPOzksg9DgE0lbqhb2e5EbU-r7naUFVEOyD8kFdsLVB8dadMi5lJPvLZPyMme-QTmNYWtu3QRABKuq2PWWh1Ag8K6nkHEqq4e4zfnhtg6c._Wf2pEZV4YOke9eJoz3FFDYf5vmSONA0cZv6eCF2TDU&dib_tag=se&keywords=resistor%2Bkit&qid=1722917981&sprefix=resistor%2Bkit%2Caps%2C106&sr=8-3&th=1)
------
</details>

<details><summary>21) 9V Battery</summary>

------
Used to power the Wrangler
- $7: [Amazon](https://www.amazon.com/Energizer-Alkaline-Volt-Battery-2-Count/dp/B004R16728/ref=sr_1_5?crid=3N2376VGJO2A0&dib=eyJ2IjoiMSJ9.by69tUnxi0q6-YnaJD-4K4OOllcvIKdu1s8krdXpCj9jQqmEn_sSGYLGry61V9zNjc5DoXxJfRU8X_jAZ0LFsWDv_ItLR3m0T6fQYUBbxZe3fQh64LcSyy_HmaQ31n1XksvQPnrOIU1kbZFVKKggYElYShhl2Iza8QhMy7tjK90MbKIB0gCjagxXdD_P38KZisHSZeUDvzcX7SpyHlzzh-TVPoqkDaj93_qXiRfdHjDz0V6PNc2qKqRP1PuVP4HzAL_t6eq7OyQzIUpu0Q4C1x4lIFUm3IQ8JNz9Evf8J9E.n843_EeWn_3Lrn85kuJHJHGck4GHF3Tw3d0BH3zPH7s&dib_tag=se&keywords=9v+battery&qid=1722918100&sprefix=9v+battery%2Caps%2C97&sr=8-5) (QTY: 2)
------
</details>

<details><summary>22) Assorted items</summary>

------
- Wire
  - 14,16,18 and regular breadboard wires were used.
  - I used higher quality 18 gauge solid copper wires for logic wires to help keep organized.
- Dupont connections (OPT)
  - I used this sometimes to terminate my 18 gauge wire when it was being used...
- Soldering Iron + Solder
------
</details>

## Total:
Price Depends on where you purchase from:
- Amazon:
    - $569
- Amazon/AliExpress:
    - $485

This price is quite steep. A major price cut could be made by choosing a different Airsoft gun, $189 price is steep.

I had most pieces lying around. I spent maybe 300$ to get this all going. My major cost was the filament.