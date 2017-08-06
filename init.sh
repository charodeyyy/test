git clone https://github.com/charodeyyy/web.git
sudo ln -sf /home/box/web/etc/default.conf /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test.conf
# /home/box/web sudo gunicorn - b 0.0.0.0:8080 hello:app
sudo /etc/init.d/gunicorn restart
