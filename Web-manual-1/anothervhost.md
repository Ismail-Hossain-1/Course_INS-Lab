
---

## 🧩 Step-by-Step Commands for `anothervhost.com`

### **1️⃣ Create the website directory**

This creates a folder structure for your new website:

```bash
sudo mkdir -p /var/www/anothervhost.com/html
```

### **2️⃣ Give ownership to your current user**

This ensures you can easily edit files in the directory:

```bash
sudo chown -R $USER:$USER /var/www/anothervhost.com/html
```

### **3️⃣ Set proper permissions**

Make sure the web directory is readable by the web server:

```bash
sudo chmod -R 755 /var/www/anothervhost.com
```

---

## 🧾 Step 4: Create the website’s home page

Open the file for editing:

```bash
nano /var/www/anothervhost.com/html/index.html
```

Then paste this content (from the earlier HTML I gave you):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Another VHost</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        main {
            padding: 20px;
            text-align: center;
        }
        footer {
            background-color: #333;
            color: white;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
        }
        h1 {
            color: #4CAF50;
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to Another Virtual Host (anothervhost.com)!</h1>
</header>

<main>
    <p>This is the home page for <strong>anothervhost.com</strong>.</p>
    <p>Here we can host different content for various websites.</p>

    <h2>Form Example</h2>
    <p>Enter your name and click "Submit" to get a greeting message:</p>
    
    <form id="greetingForm">
        Name: <input type="text" id="nameInput" placeholder="Enter your name" required>
        <button type="submit">Submit</button>
    </form>

    <p id="greetingMessage" style="margin-top: 10px; font-weight: bold;"></p>
</main>

<footer>
    <p>© 2025 Another VHost Project. All rights reserved.</p>
</footer>

<script>
    document.getElementById("greetingForm").addEventListener("submit", function(event) {
        event.preventDefault();
        
        const name = document.getElementById("nameInput").value;
        const message = document.getElementById("greetingMessage");
        
        if (name) {
            message.textContent = `Hello, ${name}! Welcome to Another VHost!`;
        } else {
            message.textContent = "Please enter a name.";
        }
    });
</script>

</body>
</html>
```

Save and exit (`CTRL + O`, `ENTER`, `CTRL + X`).

---

## ⚙️ Step 5: Create the Virtual Host configuration file

Create the configuration file:

```bash
sudo nano /etc/apache2/sites-available/anothervhost.com.conf
```

Paste this configuration:

```apache
<VirtualHost *:80>
    ServerAdmin admin@anothervhost.com
    ServerName anothervhost.com
    ServerAlias www.anothervhost.com
    DocumentRoot /var/www/anothervhost.com/html
    ErrorLog ${APACHE_LOG_DIR}/anothervhost_error.log
    CustomLog ${APACHE_LOG_DIR}/anothervhost_access.log combined
</VirtualHost>
```

Save and exit (`CTRL + O`, `ENTER`, `CTRL + X`).

---

## ✅ Step 6: Enable the new site

Enable your new virtual host configuration:

```bash
sudo a2ensite anothervhost.com.conf
```

---

## 🚫 Step 7: (Optional) Disable the default site

If you don’t want Apache to show the default page when no match is found:

```bash
sudo a2dissite 000-default.conf
```

---

## 🧪 Step 8: Test Apache configuration

Check if there are any syntax errors:

```bash
sudo apache2ctl configtest
```

You should see:

```
Syntax OK
```

---

## 🔁 Step 9: Restart Apache to apply changes

Restart the web server:

```bash
sudo systemctl restart apache2
```

---

## 🌐 Step 10: Map your domain locally

Add your new domain to `/etc/hosts` so your system knows where to find it:

```bash
sudo nano /etc/hosts
```

Add the following line:

```
127.0.0.1   anothervhost.com
```

Save and exit.

---

## 🧭 Step 11: Test in your browser

Open your browser and go to:

```
http://anothervhost.com
```

✅ You should see the custom “Welcome to Another Virtual Host” page
✅ Try submitting the form — the JavaScript will display a personalized greeting.

---

## 🏁 Summary of Commands

Here’s the **full command list** in one block for quick use:

```bash
sudo mkdir -p /var/www/anothervhost.com/html
sudo chown -R $USER:$USER /var/www/anothervhost.com/html
sudo chmod -R 755 /var/www/anothervhost.com

nano /var/www/anothervhost.com/html/index.html
# (paste HTML, save and exit)

sudo nano /etc/apache2/sites-available/anothervhost.com.conf
# (paste Apache config, save and exit)

sudo a2ensite anothervhost.com.conf
sudo a2dissite 000-default.conf  # optional
sudo apache2ctl configtest
sudo systemctl restart apache2

sudo nano /etc/hosts
# add: 127.0.0.1 anothervhost.com
```

Then open **[http://anothervhost.com](http://anothervhost.com)** in your browser.

---
