<template>
  <div class="custom-input">
    <input type="range" v-model="new_element" @input="clicked"
    :max="max_range" :min="min_range"> {{new_element}}
  </div>
</template>

<script>
export default {
  name: 'InputRange',
  props: ['el_range', 'min_range', 'max_range'],
  data() {
    return {
      new_element: this.el_range,
    };
  },
  methods: {
    clicked() {
      this.$emit('update:el_range', this.new_element);
      this.$emit('requestApi');
    },
  },
};
</script>
