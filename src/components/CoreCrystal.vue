<template>
 <v-app style="background: linear-gradient(#020203, #4e4e5e, #b8b8bf);">
  <v-container text-xs-center px-2 style="width:80vw; height:80vh;">
    <v-layout row wrap align-center col justify-center>
      <v-flex xs2>
        <h1 v-if="hover && Blade == ''" class="glow" style="font-family:helvetica; color:#84d8be; text-align:center; font_weight:thinner; opacity:90%">Click to Resonate!</h1>
        <h1 class ="name" style="font-family:helvetica; color:#84d8be; text-align:center; font_weight:thinner; opacity:90%">{{ Blade }}</h1>
        <button 
        @click="submit"
        v-if="Blade == ''"
        @mouseover="hover = true"
        @mouseleave="hover = false"
        v-on:click="1">
            <v-tooltip bottom disabled color="#a22536">
            <template v-slot:activator="{ on, attrs }">

            <v-img
          v-bind="attrs" v-on="on" 
          v-if="Blade == ''"
          src="https://vignette.wikia.nocookie.net/xenoblade/images/4/40/Core_Crystal.png/revision/latest/scale-to-width-down/340?cb=20200426104648"
          class="image"
          contain
          height="200"
            />
            </template>
            <span  style="font-family:helvetica; color:white; text-align:center; ">Click to Resonate!</span>
            </v-tooltip>


            </button>
            <transition name="fade">
            <v-img
          v-if="Blade !== ''"
          :src="Picture"

          class="pic"
          contain
            />
            </transition>

            <transition name="fade">
            <v-img
          v-if="Blade !== ''"
          :src="Element"

          class="elem"
          contain
            />
            </transition>

            <transition name="fade">
            <v-img
          v-if="Blade !== ''"
          :src="Weapon"

          class="weap"
          contain
            />
            </transition>

            <transition name="fade">
            <span
          v-if="Blade !== ''"
          class="sum"
            >"{{ Summary }}"</span>
            </transition>

            <v-btn
            v-if="Blade !== ''"
            @click="reset"
            class="tip"
            dark
            depressed
            small
            color="black"
            ><span class="new">Resonate Again?</span>
            </v-btn>

            <transition name="fade">
            <v-img
          v-if="Blade !== ''"
          src="https://i.ya-webdesign.com/images/nintendo-switch-logo-png-2.png"

          class="swi"
          contain
            />
            </transition>

            <transition name="fade">
            <a
          v-if="Blade !== ''"
          href="https://www.nintendo.com/games/detail/xenoblade-chronicles-2-switch/"
          class="lin"
          style="color:black;"
            >Buy Xenoblade Chronicles 2 Now!</a>
            </transition>

      </v-flex>
    </v-layout>
  </v-container>
 </v-app>
</template>

<script>
import axios from 'axios'
  export default {
  data() {
    return {
      Blade: '',
      Picture: '',
      Element: '',
      Weapon: '',
      Summary: '',
      hover: false,
      screenWidth: screen.width
    };
  },
    methods: {
    submit () {
      axios.get('https://apixeno.herokuapp.com/')
      .then((response) => {
        this.Blade = response.data.Blade
        this.Picture = response.data.Picture
        this.Element = response.data.Element
        this.Weapon = response.data.Weapon
        this.Summary = response.data.Summary
      })
    },
    reset () {
      this.Blade = ''
      this.hover = false
      }
}}
</script>