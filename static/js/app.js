function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {

        let dropdowns = document.getElementsByClassName("dropdown-content");
        let i;
        let openDropdown;
        for (i = 0; i < dropdowns.length; i++) {
            openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

setTimeout(myFunction, 1000);


//let p4 = document.getElementById('name')
//p4.innerHTML = name;

//let p3 = document.getElementById("descrip");
//p3.innerHTML = descrip;s

function plus() {
    number++;
    updateSpan();
}
function minus() {
    if (number != 0) {
        number--;
    }
    updateSpan();
}

function updateSpan() {
    let p = document.getElementById("p1");
    p.innerHTML = "  Кол-во товаров: " + number
    let p2 = document.getElementById("all");
    p2.innerHTML = "  Итого: " + cost1 * number + " руб"
}

function register() {
    let passw = document.getElementById("lastname").value
    let phio = document.getElementById("phio");
    let email = document.getElementById("email");
    let password = document.getElementById("password");
    let t = document.getElementById("t");
    let sale = document.getElementById("sale");
    let bonuse = document.getElementById("bonuse");
    let money = document.getElementById("money");
    if (passw == "UraAdmin")
    {
    phio.innerHTML = "ФИО: Наконечный Дмитрий Игоревич";
    email.innerHTML = "email: dinamid2008@mail.ru";
    password.innerHTML = "Пароль: " + passw;
    t.innerHTML = "Тип: Золото";
    sale.innerHTML = "Ваша скидка: 15%";
    bonuse.innerHTML = "Ваши бонусы: 3 конфеты при следующем заказе";
    money.innerHTML = "На сколько вы совершили покупки: 3125 руб";}
    else if (passw=="Danilowsk"){
    phio.innerHTML = "ФИО: Баздарев Данила";
    email.innerHTML = "email: bda.nsbr1607@yandex.ru";
    password.innerHTML = "Пароль: " + passw;
    t.innerHTML = "Тип: Cеребро";
    sale.innerHTML = "Ваша скидка: 10%";
    bonuse.innerHTML = "Ваши бонусы: нет бонусов";
    money.innerHTML = "На сколько вы совершили покупки: 108 руб";}
    else if (passw=="Lilyechka"){
    phio.innerHTML = "ФИО: Харитонова Лилия";
    email.innerHTML = "email: kharitonovalily@yandex.ru";
    password.innerHTML = "Пароль: " + passw;
    t.innerHTML = "Тип: VIP";
    sale.innerHTML = "Ваша скидка: 25%";
    bonuse.innerHTML = "Ваши бонусы: 1 конфета при каждом заказе";
    money.innerHTML = "На сколько вы совершили покупки: 128 руб";}
    else{
    phio.innerHTML = "ФИО: Неизвестно";
    email.innerHTML = "email: неизвестен";
    password.innerHTML = "Пароль: " + passw;
    t.innerHTML = "Тип: Стандарт";
    sale.innerHTML = "Ваша скидка: 0%";
    bonuse.innerHTML = "Ваши бонусы: нет";
    money.innerHTML = "На сколько вы совершили покупки: 0 руб";}
    }
