sudo ln -sf /home/box/web/etc/default.conf /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test.conf
cd /home/box/web/ask
#sudo gunicorn -b 0.0.0.0:8080 hello:hello
sudo gunicorn -c /home/sl/web/etc/gunicorn1.conf ask.wsgi:application
#sudo /etc/init.d/gunicorn restart
