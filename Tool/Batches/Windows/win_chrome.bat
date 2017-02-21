pybot -v browserName:chrome, ip:192.168.1.115, port:5550, browserVer:34.0.5 --outputdir ChromeW MultipleMachines.txt

pybot --variable name:value -v browserName:${browser} -v --NoStatusRC --exclude not_ready --outputdir my_robot_results WEB_AT\TestSuite\

pybot --variable name:value --NoStatusRC -v browser:firefox -v cfg_hubIP:192.168.1.91 -v cfg_hubPort:5550 --exclude not_ready --outputdir my_robot_results WEB_AT\TestSuite\