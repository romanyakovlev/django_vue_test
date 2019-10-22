<template>
  <div class="custom-multiselect">
  <ul>
    <li v-for="advert in adverts" v-bind:key="advert.id">
      id: {{  advert.id }};
      адрес: {{  advert.apartment_adress }};
      этаж: {{  advert.apartment_floor }};
      количество комнат: {{  advert.number_of_rooms }};
      стоимость: {{ advert.apartment_price }}
      год: {{ advert.year_of_construction }}
    </li>
  </ul>
  </div>
</template>
<script>
export default {
  name: 'ApartmentsList',
  props: ['adverts'],
};
</script>
