# KOINE-DALI

> DALI extended framework, compatible with Docker, Redis and other technologies.  

## Instrauctions
You have to put DALI subfolders into KOINE-DALI/DALI/ to make it work. 
You can find DALI at: https://github.com/AAAI-DISIM-UnivAQ/DALI.
If you need more tools, see also: https://github.com/agnsal.

1. To install SICStus Prolog see: https://sicstus.sics.se/
2. To download KOINE-DALI and its dependencies:
```sh
  git clone https://github.com/agnsal/KOINE-DALI.git
  cd KOINE-DALI/DALI
  git clone https://github.com/AAAI-DISIM-UnivAQ/DALI.git
  mv DALI/* .
  rm -rf DALI
```
3. To make a test by starting the example MAS:
```sh
  cd KOINE-MAS-example/conf
  chmod u+rx makeconf.sh
  chmod u+rx startagent.sh
  cd ..
  bash startmasMary.sh
```
Press a button to stop the example MAS.

4. If you want to create your own MAS:
- Copy the KOINE-MAS-example folder and rename it as you want.
- Change KOINE-MAS-example/mas content with your own MAS.
- Repeat the step number 3 for your new project folder.
