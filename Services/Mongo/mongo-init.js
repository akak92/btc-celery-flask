
/*
Pedro Díaz - Junio 2024
    Script de inicialización de MongoDB.
    Creamos DB nombre 'BTC-PRICES'
    Creamos colecciones con los precios de interés.

    De momento, creamos colecciones para los precios de BTC para:
    Peso Argentino ('btcars')
    Real Brasileño ('btcbrl')
    Dolar Estadounidense ('btcusd')
    Euro ('btceur')
    Corona Danesa ('brcdkk')
    Yen Japonés ('btcjpy')
    Rusia ('btcrub')
    Peso mexicano ('btcmxn')
    Peso Uruguayo ('btcuyu')
    Peso Chileno ('btcclp')
    Rupia india ('btcinr')
*/

db = db.getSiblingDB('BTC-PRICES');
db.create_collection('btcars');
db.create_collection('btcusd');
db.create_collection('btceur');
db.create_collection('btcbrl');
db.create_collection('btcdkk');
db.create_collection('btcjpy');
db.create_collection('btcrub');
db.create_collection('btcmxn');
db.create_collection('btcuyu');
db.create_collection('btcclp');
db.create_collection('btcinr');