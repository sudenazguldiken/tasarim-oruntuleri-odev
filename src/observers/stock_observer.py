# -*- coding: utf-8 -*-
from src.observers.observer import Observer

class StockObserver(Observer):
    def update(self, event, data):
        if event == 'item_added':
            print('[STOK] ' + data['name'] + ' urun sepete eklendi, stok guncelleniyor...')
