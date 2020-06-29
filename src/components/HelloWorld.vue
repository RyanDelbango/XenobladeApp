<template>
 <v-app style="background: linear-gradient(#020203, #4e4e5e, #b8b8bf);">
  <v-container text-xs-center px-2>
    <v-layout row wrap align-center col justify-center>
      <v-flex xs2>
        <h1 v-if="hover" style="font-family:helvetica; color:	#84d8be; text-align:center; font_weight:thinner; opacity:90%">Click to Resonate!</h1>
        <button 
        @mouseover="hover = true"
        @mouseleave="hover = false"
        v-on:click="1">
            <v-tooltip bottom disabled color="#a22536">
            <template v-slot:activator="{ on, attrs }">

            <v-img
          v-bind="attrs" v-on="on" 
          src="https://vignette.wikia.nocookie.net/xenoblade/images/4/40/Core_Crystal.png/revision/latest/scale-to-width-down/340?cb=20200426104648"
          class="image"
          contain
          height="200"
            />
            </template>
            <span  style="font-family:helvetica; color:white; text-align:center; ">Click to Resonate!</span>
            </v-tooltip>


            </button>

      </v-flex>
    </v-layout>
  </v-container>
 </v-app>
</template>

<script>
  export default {
  data() {
    return {
      hover: false,
    };
  }
}
</script>