document.addEventListener('DOMContentLoaded', function() {
  const phoneInput = document.getElementById('id_phone');
  
  phoneInput.addEventListener('input', function(e) {
    // Удаляем все нецифровые символы, кроме ведущего +
    let phoneNumber = e.target.value.replace(/[^\d+]/g, '');
    
    // Если номер начинается не с +7, добавляем +7
    if (!phoneNumber.startsWith('+7')) {
      phoneNumber = '+7' + phoneNumber.replace(/\D/g, '');
    }
    
    // Ограничиваем длину (11 цифр: +7 и 10 цифр номера)
    const digitsOnly = phoneNumber.replace(/\D/g, '');
    if (digitsOnly.length > 11) {
      phoneNumber = phoneNumber.substring(0, phoneNumber.length - (digitsOnly.length - 12));
    }
    
    // Форматируем номер
    let formattedPhone = '+7';
    const cleanNumber = phoneNumber.replace(/\D/g, '').substring(1); // Убираем +7
    console.log(cleanNumber);
    
    if (cleanNumber.length > 0) {
      formattedPhone += ' (' + cleanNumber.substring(0, 3);
    }
    if (cleanNumber.length > 3) {
      formattedPhone += ') ' + cleanNumber.substring(3, 6);
    }
    if (cleanNumber.length > 6) {
      formattedPhone += '-' + cleanNumber.substring(6, 8);
    }
    if (cleanNumber.length > 8) {
      formattedPhone += '-' + cleanNumber.substring(8, 10);
    }
    
    // Устанавливаем отформатированное значение
    e.target.value = formattedPhone;
  });
  
  // Обработчик для корректного удаления
  phoneInput.addEventListener('keydown', function(e) {
    if (e.key === 'Backspace' && /\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$/.test(e.target.value)) {
      // Позволяем удалить последнюю цифру без скобок/дефисов
      e.target.value = e.target.value.slice(0, -1);
      e.preventDefault();
    }
  });
});