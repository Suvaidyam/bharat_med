<template>
	<div class="min-h-screen p-4 sm:p-6 md:p-8">
		<div class="">
			<!-- Navigation Tabs -->
			<div class="mb-6">
				<nav class="flex space-x-1" aria-label="Tabs">
					<button
						v-for="tab in tabs"
						:key="tab.name"
						:class="[
							tab.current
								? 'bg-gray-200 text-gray-800'
								: 'text-gray-600 hover:text-gray-800 hover:bg-gray-100',
							'px-4 py-2 font-medium text-sm rounded-sm',
						]"
					>
						{{ tab.name }}
					</button>
				</nav>
			</div>

			<!-- Main Form Container -->
			<div class="bg-white p-6 sm:p-8 rounded-sm shadow-md">
				<div class="mb-8">
					<h1 class="text-2xl font-bold text-gray-900">Personal Information</h1>
					<p class="mt-1 text-sm text-gray-600">
						Enter the staff member's basic personal information
					</p>
				</div>

				<form @submit.prevent="saveAndContinue">
					<div class="grid grid-cols-1 md:grid-cols-4 gap-x-8 gap-y-6">
						<!-- Upload Photo -->
						<div class="md:col-span-1">
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Upload photo</label
							>
							<div
								class="mt-1 flex justify-center items-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-sm h-40"
							>
								<div class="space-y-1 text-center">
									<svg
										class="mx-auto h-12 w-12 text-gray-400"
										stroke="currentColor"
										fill="none"
										viewBox="0 0 48 48"
										aria-hidden="true"
									>
										<path
											d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8"
											stroke-width="2"
											stroke-linecap="round"
											stroke-linejoin="round"
										/>
									</svg>
									<p class="text-sm text-gray-600">
										<button
											type="button"
											class="font-medium text-indigo-600 hover:text-indigo-500"
										>
											Upload a file
										</button>
									</p>
									<p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
								</div>
							</div>
						</div>

						<!-- Personal Info Fields -->
						<div class="md:col-span-3 grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-6">
							<div>
								<label
									for="first-name"
									class="block text-sm font-medium text-gray-700"
									>First Name</label
								>
								<input
									type="text"
									v-model="form.firstName"
									id="first-name"
									placeholder="Enter first name"
									class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
								/>
							</div>

							<div>
								<label
									for="last-name"
									class="block text-sm font-medium text-gray-700"
									>Last Name</label
								>
								<input
									type="text"
									v-model="form.lastName"
									id="last-name"
									placeholder="Enter last name"
									class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
								/>
							</div>

							<div>
								<label for="dob" class="block text-sm font-medium text-gray-700"
									>Date of Birth</label
								>
								<input
									type="text"
									v-model="form.dob"
									id="dob"
									placeholder="Select date"
									class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
								/>
							</div>

							<div>
								<label for="gender" class="block text-sm font-medium text-gray-700"
									>Gender</label
								>
								<select
									v-model="form.gender"
									id="gender"
									class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
								>
									<option disabled value="">Select gender</option>
									<option>Male</option>
									<option>Female</option>
									<option>Other</option>
									<option>Prefer not to say</option>
								</select>
							</div>
						</div>

						<!-- Email Address -->
						<div class="md:col-span-2">
							<label for="email" class="block text-sm font-medium text-gray-700"
								>Email Address</label
							>
							<div class="mt-1 relative rounded-sm shadow-sm">
								<div
									class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3"
								>
									<svg
										class="h-5 w-5 text-gray-400"
										xmlns="http://www.w3.org/2000/svg"
										viewBox="0 0 20 20"
										fill="currentColor"
									>
										<path
											d="M3 4a2 2 0 00-2 2v1.161l8.441 4.221a1.25 1.25 0 001.118 0L19 7.162V6a2 2 0 00-2-2H3z"
										/>
										<path
											d="M19 8.839l-7.77 3.885a2.75 2.75 0 01-2.46 0L1 8.839V14a2 2 0 002 2h14a2 2 0 002-2V8.839z"
										/>
									</svg>
								</div>
								<input
									type="email"
									v-model="form.email"
									id="email"
									class="block w-full rounded-sm border-gray-300 pl-10 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
									placeholder="Enter email address"
								/>
							</div>
						</div>

						<!-- Phone Number -->
						<div class="md:col-span-2">
							<label for="phone" class="block text-sm font-medium text-gray-700"
								>Phone Number</label
							>
							<div class="mt-1 relative rounded-sm shadow-sm">
								<div
									class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3"
								>
									<svg
										class="h-5 w-5 text-gray-400"
										xmlns="http://www.w3.org/2000/svg"
										fill="none"
										viewBox="0 0 24 24"
										stroke-width="1.5"
										stroke="currentColor"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 6.75z"
										/>
									</svg>
								</div>
								<input
									type="tel"
									v-model="form.phone"
									id="phone"
									class="block w-full rounded-sm border-gray-300 pl-10 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
									placeholder="Enter phone number"
								/>
							</div>
						</div>

						<!-- Address -->
						<div class="md:col-span-4">
							<label for="address" class="block text-sm font-medium text-gray-700"
								>Address</label
							>
							<div class="mt-1 relative rounded-sm shadow-sm">
								<div
									class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3"
								>
									<svg
										class="h-5 w-5 text-gray-400"
										xmlns="http://www.w3.org/2000/svg"
										viewBox="0 0 20 20"
										fill="currentColor"
									>
										<path
											fill-rule="evenodd"
											d="M9.69 18.933l.003.001C9.89 19.02 10 19 10 19s.11.02.308-.066l.002-.001.006-.003.018-.008a5.741 5.741 0 00.281-.14c.186-.1.4-.27.663-.513l6.01-6.01a1.5 1.5 0 00-2.122-2.122l-6.01 6.01a1.5 1.5 0 002.122 2.122l.006.006z"
											clip-rule="evenodd"
										/>
										<path
											d="M10 18a8 8 0 100-16 8 8 0 000 16zm.707-10.293a1 1 0 00-1.414-1.414l-3 3a1 1 0 000 1.414l3 3a1 1 0 001.414-1.414L9.414 11H13a1 1 0 100-2H9.414l1.293-1.293z"
										/>
									</svg>
								</div>
								<input
									type="text"
									v-model="form.address"
									id="address"
									class="block w-full rounded-sm border-gray-300 pl-10 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
									placeholder="Enter address"
								/>
							</div>
						</div>

						<!-- City -->
						<div class="md:col-span-2">
							<label for="city" class="block text-sm font-medium text-gray-700"
								>City</label
							>
							<input
								type="text"
								v-model="form.city"
								id="city"
								placeholder="Enter city"
								class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							/>
						</div>

						<!-- State/Province -->
						<div class="md:col-span-2">
							<label for="state" class="block text-sm font-medium text-gray-700"
								>State/Province</label
							>
							<input
								type="text"
								v-model="form.state"
								id="state"
								placeholder="Enter state or province"
								class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							/>
						</div>

						<!-- Postal Code -->
						<div class="md:col-span-2">
							<label
								for="postal-code"
								class="block text-sm font-medium text-gray-700"
								>Postal Code</label
							>
							<input
								type="text"
								v-model="form.postalCode"
								id="postal-code"
								placeholder="Enter postal code"
								class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							/>
						</div>

						<!-- Country -->
						<div class="md:col-span-2">
							<label for="country" class="block text-sm font-medium text-gray-700"
								>Country</label
							>
							<select
								v-model="form.country"
								id="country"
								class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							>
								<option disabled value="">Select country</option>
								<option>United States</option>
								<option>Canada</option>
								<option>Mexico</option>
								<option>United Kingdom</option>
							</select>
						</div>

						<!-- Emergency Contact Section -->
						<div class="md:col-span-4 pt-4 border-t border-gray-200 mt-2">
							<h3 class="text-lg font-medium leading-6 text-gray-900">
								Emergency Contact
							</h3>
						</div>

						<div class="md:col-span-2">
							<label
								for="emergency-contact-name"
								class="block text-sm font-medium text-gray-700"
								>Contact name</label
							>
							<input
								type="text"
								v-model="form.emergencyContactName"
								id="emergency-contact-name"
								placeholder="Contact name"
								class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							/>
						</div>
						<div class="md:col-span-2">
							<label
								for="emergency-contact-phone"
								class="block text-sm font-medium text-gray-700"
								>Contact phone</label
							>
							<input
								type="tel"
								v-model="form.emergencyContactPhone"
								id="emergency-contact-phone"
								placeholder="Contact phone"
								class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							/>
						</div>
						<div class="md:col-span-2">
							<label
								for="emergency-contact-relationship"
								class="block text-sm font-medium text-gray-700"
								>Relationship</label
							>
							<input
								type="text"
								v-model="form.emergencyContactRelationship"
								id="emergency-contact-relationship"
								placeholder="Relationship"
								class="mt-1 block w-full rounded-sm border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							/>
						</div>
					</div>

					<!-- Form Actions -->
					<div class="mt-10 flex items-center justify-between">
						<button
							type="button"
							@click="cancel"
							class="rounded-sm bg-white py-2 px-4 text-sm font-medium text-gray-700 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
						>
							Cancel
						</button>
						<button
							type="submit"
							class="inline-flex items-center gap-x-2 rounded-sm bg-gray-800 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-900"
						>
							<svg
								class="h-5 w-5"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 20 20"
								fill="currentColor"
							>
								<path
									d="M3.75 3.75A.75.75 0 003 4.5v11a.75.75 0 00.75.75h13.5a.75.75 0 00.75-.75v-7a.75.75 0 00-1.5 0v6.25H4.5V4.5h6.25a.75.75 0 000-1.5H3.75z"
								/>
								<path
									d="M10.75 3.75a.75.75 0 000 1.5h2.793l-6.147 6.146a.75.75 0 001.06 1.06L15 6.06v2.793a.75.75 0 001.5 0V3.75h-5.75z"
								/>
								<path
									d="M10.75 3.75a.75.75 0 000 1.5h2.793l-6.147 6.146a.75.75 0 001.06 1.06L15 6.06v2.793a.75.75 0 001.5 0V3.75h-5.75z"
								/>
								<path
									d="M3.75 3.75A.75.75 0 003 4.5v11a.75.75 0 00.75.75h13.5a.75.75 0 00.75-.75v-7a.75.75 0 00-1.5 0v6.25H4.5V4.5h6.25a.75.75 0 000-1.5H3.75zM14 3a1 1 0 00-1-1H5a1 1 0 00-1 1v14a1 1 0 001 1h10a1 1 0 001-1V7.414A1 1 0 0015.414 7L12 3.586A1 1 0 0012.414 3H14zM5 4h6v4h4v8H5V4z"
								/>
								<path
									d="M3 3.5A1.5 1.5 0 014.5 2h6.879a1.5 1.5 0 011.06.44l4.122 4.12A1.5 1.5 0 0117 7.621V16.5A1.5 1.5 0 0115.5 18h-11A1.5 1.5 0 013 16.5v-13zM4.5 3a.5.5 0 00-.5.5v13a.5.5 0 00.5.5h11a.5.5 0 00.5-.5V7.621a.5.5 0 00-.146-.353l-4.122-4.122A.5.5 0 0011.379 3H4.5z"
								/>
								<path
									d="M8 7a1 1 0 011-1h.01a1 1 0 110 2H9a1 1 0 01-1-1zm3 0a1 1 0 011-1h2a1 1 0 110 2h-2a1 1 0 01-1-1z"
								/>
							</svg>
							Save & Continue
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, reactive } from 'vue'

// Tab navigation data
const tabs = ref([
	{ name: 'Personal Info', current: true },
	{ name: 'Professional', current: false },
	{ name: 'Employment', current: false },
	{ name: 'Access & Roles', current: false },
])

// Form data model
const form = reactive({
	firstName: '',
	lastName: '',
	dob: 'Thu Jun 26 2025', // Pre-filled as in the image
	gender: '',
	email: '',
	phone: '',
	address: '',
	city: '',
	state: '',
	postalCode: '',
	country: '',
	emergencyContactName: '',
	emergencyContactPhone: '',
	emergencyContactRelationship: '',
})

// Methods
function saveAndContinue() {
	// Handle form submission logic
	console.log('Form Submitted:', form)
	// You would typically send this data to an API
	alert('Form data has been logged to the console.')
}

function cancel() {
	// Handle cancellation logic
	console.log('Form cancelled')
	// Optional: Reset form fields
	Object.keys(form).forEach((key) => (form[key] = ''))
	form.dob = 'Thu Jun 26 2025'
	form.gender = ''
	form.country = ''
}
</script>

<style>
/* For the custom select arrow, if needed. Tailwind Forms plugin handles this well. */
select {
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
	background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20"><path stroke="%236b7280" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M6 8l4 4 4-4"/></svg>');
	background-position: right 0.5rem center;
	background-repeat: no-repeat;
	background-size: 1.5em 1.5em;
	padding-right: 2.5rem;
}
</style>
