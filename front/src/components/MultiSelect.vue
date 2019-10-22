<template>
  <div class="custom-multiselect">

  <select v-model="new_element" multiple @change="clicked">
      <option v-for="el in arr_els" v-bind:key="el">{{el}}</option>
  </select> {{new_element}}

  </div>
</template>

<script>
export default {
  name: 'MultiSelect',
  props: ['sel_element', 'arr_els'],
  data() {
    return {
      new_element: [],
    };
  },
  methods: {
    clicked() {
      this.$emit('update:sel_element', this.new_element);
      this.$emit('requestApi');
    },
  },
};
</script>
