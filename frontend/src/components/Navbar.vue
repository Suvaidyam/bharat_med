<template>
	<nav class="bg-[#001f3f] text-white px-4 py-3 flex items-center justify-between relative">
		<div class="flex items-center">
			<!-- Logo and Title -->
			<div class="flex items-center gap-[20px !important] px-4">
				<!-- <img src="@/assets/logo.png" alt="Logo" class="w-6 h-6" /> -->
				<span class="font-bold text-lg">Coop<span class="text-white">Connect</span></span>
			</div>

			<!-- Navigation Links (Desktop) -->
			<div class="hidden md:flex items-center space-x-6 text-sm">
				<a href="#" class="hover:text-gray-300">Home</a>
				<a href="#" class="hover:text-gray-300">About Us</a>
				<a href="#" class="hover:text-gray-300">Features</a>
				<a href="/faqs" class="hover:text-gray-300">FAQs</a>
			</div>
		</div>
		<div class="flex items-center space-x-4">
			<!-- Language Dropdown -->
			<!-- <div class="relative">
				<button
					@click="toggleDropdown"
					class="bg-white text-black px-3 py-1 rounded-md text-sm flex items-center"
				>
					EN
					<svg class="w-4 h-4 ml-1" fill="currentColor" viewBox="0 0 20 20">
						<path
							fill-rule="evenodd"
							d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4.24 4.24a.75.75 0 01-1.06 0L5.21 8.27a.75.75 0 01.02-1.06z"
							clip-rule="evenodd"
						/>
					</svg>
				</button>
				<div
					v-if="showDropdown"
					class="absolute right-0 mt-2 w-20 bg-white text-black rounded shadow-lg z-10"
				>
					<a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">EN</a>
					<a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">FR</a>
					<a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">ES</a>
				</div>
			</div> -->
			<!-- Language Dropdown -->
			<div class="">
				<Dropdown
					:options="[
						{
							label: 'EN',
							onClick: () => {},
						},
						{
							label: 'FR',
							onClick: () => {},
						},
						{
							label: 'ES',
							onClick: () => {},
						},
					]"
					:button="{
						label: 'EN',
					}"
				/>
			</div>

			<!-- Login Dropdown -->
			<div class="" v-if="session.isLoggedIn">
				<Dropdown
					:options="[
						{
							label: 'Profile',
							onClick: () => {},
						},
						{
							label: 'Logout',
							onClick: () => {
								session.logout.submit()
							},
						},
					]"
					:button="{
						label: session.user?.charAt(0).toUpperCase(),
					}"
				/>
			</div>
			<div class="" v-else>
				<Dropdown
					:options="[
						{
							label: 'Login Doctor',
							onClick: () => {
								console.log('Doctor Login')
								router.push('/login')
							},
						},
						{
							label: 'Login Patient',
							onClick: () => {
								router.push('/login')
							},
						},
					]"
					:button="{
						label: 'Login',
					}"
				/>
			</div>
		</div>

		<!-- Hamburger for Mobile -->
		<button class="md:hidden ml-4 text-white" @click="toggleMobile">
			<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M4 6h16M4 12h16M4 18h16"
				/>
			</svg>
		</button>

		<!-- Mobile Links -->
		<div
			v-if="mobileOpen"
			class="absolute top-13 left-0 w-full bg-[#001f3f] text-white p-4 md:hidden z-20 flex flex-col"
			@click="toggleMobile"
			@click.stop
		>
			<a href="#" class="hover:text-gray-300">Home</a>
			<a href="#" class="hover:text-gray-300">About Us</a>
			<a href="#" class="hover:text-gray-300">Features</a>
			<a href="#" class="hover:text-gray-300">FAQs</a>
		</div>
	</nav>
</template>

<script setup>
import { ref, inject } from 'vue'
import { useRouter } from 'vue-router'
import { Dropdown } from 'frappe-ui'
const session = inject('$session')
const router = useRouter()

const showDropdown = ref(false)
const mobileOpen = ref(false)

const toggleDropdown = () => {
	showDropdown.value = !showDropdown.value
}

const toggleMobile = () => {
	mobileOpen.value = !mobileOpen.value
}
</script>
