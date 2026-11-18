# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import zipfile
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_DIR = os.path.join(BASE_DIR, "apk_build")
SDK_DIR = r"C:\Users\rajan\AppData\Local\Android\Sdk"
BUILD_TOOLS = os.path.join(SDK_DIR, r"build-tools\35.0.0")
ANDROID_JAR = os.path.join(SDK_DIR, r"platforms\android-36\android.jar")
JDK_BIN = r"C:\Program Files\Android\Android Studio\jbr\bin"

AAPT2 = os.path.join(BUILD_TOOLS, "aapt2.exe")
D8 = os.path.join(BUILD_TOOLS, "d8.bat")
ZIPALIGN = os.path.join(BUILD_TOOLS, "zipalign.exe")
APKSIGNER = os.path.join(BUILD_TOOLS, "apksigner.bat")
JAVAC = os.path.join(JDK_BIN, "javac.exe")
KEYTOOL = os.path.join(JDK_BIN, "keytool.exe")
JAVA_HOME = os.path.dirname(JDK_BIN)

PACKAGE = "com.nexedu.childrensday2026"
APP_NAME = "Nex Edu Games"

def run_cmd(cmd, desc=""):
    print(f"--> {desc}: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    env = os.environ.copy()
    env["JAVA_HOME"] = JAVA_HOME
    env["PATH"] = JDK_BIN + ";" + env.get("PATH", "")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
    if res.returncode != 0:
        print(f"STDOUT: {res.stdout}")
        print(f"STDERR: {res.stderr}")
        raise RuntimeError(f"Command failed: {desc}")
    return res.stdout

def setup_dirs():
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(os.path.join(BUILD_DIR, "src", "main", "assets"), exist_ok=True)
    os.makedirs(os.path.join(BUILD_DIR, "src", "main", "res", "values"), exist_ok=True)
    os.makedirs(os.path.join(BUILD_DIR, "src", "main", "java", "com", "nexedu", "childrensday2026"), exist_ok=True)
    os.makedirs(os.path.join(BUILD_DIR, "gen"), exist_ok=True)
    os.makedirs(os.path.join(BUILD_DIR, "bin"), exist_ok=True)
    os.makedirs(os.path.join(BUILD_DIR, "dist"), exist_ok=True)

def generate_icons():
    logo_path = os.path.join(BASE_DIR, "logo.jpg")
    img = Image.open(logo_path)
    sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }
    for folder, size in sizes.items():
        folder_path = os.path.join(BUILD_DIR, "src", "main", "res", folder)
        os.makedirs(folder_path, exist_ok=True)
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(os.path.join(folder_path, "ic_launcher.png"), "PNG")

def write_manifest_and_res():
    # AndroidManifest.xml
    manifest_content = f'''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="{PACKAGE}"
    android:versionCode="1"
    android:versionName="1.0.0">

    <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="35" />

    <application
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher"
        android:hardwareAccelerated="true"
        android:supportsRtl="true"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen">
        
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:configChanges="orientation|screenSize|keyboardHidden|screenLayout|smallestScreenSize"
            android:screenOrientation="sensor">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
'''
    with open(os.path.join(BUILD_DIR, "src", "main", "AndroidManifest.xml"), "w", encoding="utf-8") as f:
        f.write(manifest_content)

    # strings.xml
    strings_content = f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">{APP_NAME}</string>
</resources>
'''
    with open(os.path.join(BUILD_DIR, "src", "main", "res", "values", "strings.xml"), "w", encoding="utf-8") as f:
        f.write(strings_content)

    # MainActivity.java
    java_content = '''package com.nexedu.childrensday2026;

import android.app.Activity;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        
        webView = new WebView(this);
        setContentView(webView);
        
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setUseWideViewPort(true);
        settings.setLoadWithOverviewMode(true);
        settings.setMediaPlaybackRequiresUserGesture(false);
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);

        webView.setWebViewClient(new WebViewClient());
        webView.loadUrl("file:///android_asset/index.html");
    }

    @Override
    public void onBackPressed() {
        if (webView != null && webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
'''
    with open(os.path.join(BUILD_DIR, "src", "main", "java", "com", "nexedu", "childrensday2026", "MainActivity.java"), "w", encoding="utf-8") as f:
        f.write(java_content)

    # Copy HTML to assets
    src_html = os.path.join(BASE_DIR, "NexEdu_ChildrensDay_Games.html")
    dst_html = os.path.join(BUILD_DIR, "src", "main", "assets", "index.html")
    shutil.copyfile(src_html, dst_html)

def build_apk():
    setup_dirs()
    print("1. Directories prepared.")
    
    generate_icons()
    print("2. App icons generated from Nex Edu Logo.")
    
    write_manifest_and_res()
    print("3. Android Manifest, resources, and MainActivity written.")

    res_dir = os.path.join(BUILD_DIR, "src", "main", "res")
    compiled_res = os.path.join(BUILD_DIR, "compiled_res.zip")
    manifest_xml = os.path.join(BUILD_DIR, "src", "main", "AndroidManifest.xml")
    assets_dir = os.path.join(BUILD_DIR, "src", "main", "assets")
    gen_dir = os.path.join(BUILD_DIR, "gen")
    bin_dir = os.path.join(BUILD_DIR, "bin")
    unaligned_apk = os.path.join(BUILD_DIR, "unaligned.apk")
    aligned_apk = os.path.join(BUILD_DIR, "aligned.apk")
    final_apk = os.path.join(BASE_DIR, "NexEdu_ChildrensDay_2026.apk")

    # 4. Compile Resources with aapt2
    run_cmd(f'"{AAPT2}" compile --dir "{res_dir}" -o "{compiled_res}"', "Compile Resources")

    # 5. Link Resources & Assets with aapt2
    run_cmd(
        f'"{AAPT2}" link -I "{ANDROID_JAR}" --manifest "{manifest_xml}" -o "{unaligned_apk}" "{compiled_res}" -A "{assets_dir}" --java "{gen_dir}"',
        "Link Resources & Create Base APK"
    )

    # 6. Compile Java code
    r_java = os.path.join(gen_dir, "com", "nexedu", "childrensday2026", "R.java")
    main_java = os.path.join(BUILD_DIR, "src", "main", "java", "com", "nexedu", "childrensday2026", "MainActivity.java")
    run_cmd(
        f'"{JAVAC}" -d "{bin_dir}" -cp "{ANDROID_JAR}" "{r_java}" "{main_java}"',
        "Compile Java Source to .class"
    )

    # 7. Convert .class to DEX with d8
    class_files = [
        os.path.join(bin_dir, "com", "nexedu", "childrensday2026", "R.class"),
        os.path.join(bin_dir, "com", "nexedu", "childrensday2026", "MainActivity.class")
    ]
    class_args = " ".join([f'"{cf}"' for cf in class_files if os.path.exists(cf)])
    # Also include any inner classes
    com_dir = os.path.join(bin_dir, "com", "nexedu", "childrensday2026")
    for f in os.listdir(com_dir):
        full_f = os.path.join(com_dir, f)
        if full_f not in class_files and f.endswith(".class"):
            class_args += f' "{full_f}"'
            
    run_cmd(
        f'"{D8}" --output "{bin_dir}" {class_args} --lib "{ANDROID_JAR}"',
        "Convert Bytecode to classes.dex"
    )

    # 8. Add classes.dex to unaligned.apk
    dex_path = os.path.join(bin_dir, "classes.dex")
    with zipfile.ZipFile(unaligned_apk, 'a') as apk_zip:
        apk_zip.write(dex_path, "classes.dex")
    print("8. classes.dex added into APK.")

    # 9. Zipalign APK
    run_cmd(f'"{ZIPALIGN}" -p -f 4 "{unaligned_apk}" "{aligned_apk}"', "Zipalign APK")

    # 10. Generate Keystore if not exists
    keystore_path = os.path.join(BUILD_DIR, "release.keystore")
    if not os.path.exists(keystore_path):
        run_cmd(
            f'"{KEYTOOL}" -genkeypair -v -keystore "{keystore_path}" -alias nexedu -keyalg RSA -keysize 2048 -validity 10000 -storepass nexedu2026 -keypass nexedu2026 -dname "CN=Nex Edu, OU=Education, O=Nex Edu Classes, L=Kolkata, ST=WB, C=IN"',
            "Generate Signing Keystore"
        )

    # 11. Sign APK with apksigner
    run_cmd(
        f'"{APKSIGNER}" sign --ks "{keystore_path}" --ks-pass pass:nexedu2026 --key-pass pass:nexedu2026 --ks-key-alias nexedu --out "{final_apk}" "{aligned_apk}"',
        "Sign APK with apksigner"
    )

    print("\n=======================================================")
    print(f"🎉 SUCCESS! APK created at: {final_apk}")
    print(f"Size: {os.path.getsize(final_apk):,} bytes")
    print("=======================================================")

if __name__ == "__main__":
    build_apk()
