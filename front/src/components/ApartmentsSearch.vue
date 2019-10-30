<template>
  <div class="home">

    <div v-if="everthing_is_ready">

      не первый/последний этаж <Checkbox :toggle.sync="toggle"
      @requestApi="getApartmentsListThrottled"/>

      нижняя цена <InputRange :el_range.sync="low_price"
      @requestApi="getApartmentsListThrottled"
      :min-range="selected_low_price" :max_range="selected_high_price"/>

      верхняя цена <InputRange :el_range.sync="high_price"
      @requestApi="getApartmentsListThrottled"
      :min-range="selected_low_price" :max_range="selected_high_price"/>

      нижний этаж <InputRange :el_range.sync="low_floor"
      @requestApi="getApartmentsListThrottled"
      :min-range="selected_low_floor" :max_range="selected_high_floor"/>

      верхний этаж <InputRange :el_range.sync="high_floor"
      @requestApi="getApartmentsListThrottled"
      :min-range="selected_low_floor" :max_range="selected_high_floor"/>

      <MultiSelect :sel_element.sync="selected_rooms" :arr_els="rooms"
      @requestApi="getApartmentsListThrottled"/>

      <MultiSelect :sel_element.sync="selected_years" :arr_els="years"
      @requestApi="getApartmentsListThrottled"/>

    </div>

    <h3>Всего объявлений: {{ad_count}} </h3>

    <ApartmentsList :adverts="adverts"/>

    <Pagination :pages="pages" :getPage="getApartmentsList"/>

  </div>
</template>

<script>
import axios from 'axios';
import Checkbox from '@/components/CheckBox.vue';
import InputRange from '@/components/InputRange.vue';
import MultiSelect from '@/components/MultiSelect.vue';
import ApartmentsList from '@/components/ApartmentsList.vue';
import Pagination from '@/components/Pagination.vue';
import throttle from '@/utils/throttle';

export default {
  name: 'ApartmentsSearch',
  data() {
    return {
      adverts: [],
      rooms: [],
      selected_rooms: [],
      toggle: false,
      low_price: 0,
      high_price: 0,
      years: [],
      selected_years: [],
      low_floor: 0,
      high_floor: 0,
      selected_low_price: 0,
      selected_high_price: 0,
      selected_low_floor: 0,
      selected_high_floor: 0,
      ad_count: 0,
      next_page: null,
      previous_page: null,
      total_pages: 0,
      pages: [],
      everthingIsReady: false,
    };
  },
  methods: {
    getApartmentsList(page = 1) {
      this.page = page;
      const path = 'http://localhost:5000/api/apartments/';
      const params = new URLSearchParams({
        toggle: this.toggle,
        low_price: this.low_price,
        high_price: this.high_price,
        low_floor: this.low_floor,
        high_floor: this.high_floor,
        page: this.page,
      });
      // append rooms
      for (let i = 0; i < this.selected_rooms.length; i += 1) {
        params.append('rooms', this.selected_rooms[i]);
      }
      // append years
      for (let i = 0; i < this.selected_years.length; i += 1) {
        params.append('years', this.selected_years[i]);
      }
      axios
        .get(path, { params })
        .then((res) => {
          this.adverts = res.data.results;
          this.ad_count = res.data.count;
          this.total_pages = res.data.total_pages;
          this.getPagination();
        })
        .catch((error) => { console.error(error); });
    },
    getSearchParams() {
      const path = 'http://localhost:5000/get_init_data/';
      axios
        .get(path)
        .then((res) => {
          this.high_price = res.data.apartment_price__max;
          this.selected_high_price = res.data.apartment_price__max;
          this.low_price = res.data.apartment_price__min;
          this.selected_low_price = res.data.apartment_price__min;
          this.years = res.data.years_of_construction;
          this.rooms = res.data.number_of_rooms;
          this.low_floor = res.data.apartment_floor__min;
          this.selected_low_floor = res.data.apartment_floor__min;
          this.high_floor = res.data.apartment_floor__max;
          this.selected_high_floor = res.data.apartment_floor__max;
          this.everthing_is_ready = true;
          this.getApartmentsList();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getPagination() {
      this.pages = [];
      for (let i = 1; i <= this.total_pages; i += 1) {
        this.pages += i;
      }
    },
  },
  created() {
    this.getSearchParams();
  },
  computed: {
    getApartmentsListThrottled() {
      const DELAY = 1000;
      return throttle(this.getApartmentsList, DELAY);
    },
  },
  components: {
    Checkbox,
    InputRange,
    MultiSelect,
    ApartmentsList,
    Pagination,
  },
};
</script>
