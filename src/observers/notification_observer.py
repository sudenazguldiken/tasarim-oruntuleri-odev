# -*- coding: utf-8 -*-
from src.observers.observer import Observer

class NotificationObserver(Observer):
    def update(self, event, data):
        if event == 'item_added':
            print('[BILDIRIM] Sepetinize ' + data['name'] + ' eklendi!')
        elif event == 'discount_applied':
            print('[BILDIRIM] Indirim uygulandı: ' + data['code'])
