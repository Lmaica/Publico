from datetime import datetime,timedelta

from tkinter import ttk
import tkcalendar as tc
from tkinter import StringVar
from tkinter import messagebox
import tkinter as tk
from tkinter import IntVar

import os
import sqlite3
from time import sleep
from babel.numbers import *


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import urllib.parse
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW

import pygetwindow

import pyautogui as py
import pygetwindow as gw
import clipboard as pc
from pyperclip import *
import webbrowser