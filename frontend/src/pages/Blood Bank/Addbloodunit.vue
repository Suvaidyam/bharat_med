<template>
	<div class="min-h-screen py-8 px-4 sm:px-6 lg:px-8">
		<div class="">
			<!-- Header -->
			<div class="flex justify-between items-start mb-8">
				<div>
					<h1 class="text-3xl font-bold text-gray-900 mb-2">Add Blood Unit</h1>
					<p class="text-gray-600">Add a new blood unit to the blood bank inventory</p>
				</div>
				<button
					@click="handleCancel"
					class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
				>
					Cancel
				</button>
			</div>

			<!-- Form Container -->
			<div class="bg-white shadow-lg rounded-lg overflow-hidden">
				<div class="px-6 py-8">
					<h2 class="text-xl font-semibold text-gray-900 mb-4">
						Blood Unit Information
					</h2>
					<p class="text-sm text-gray-600 mb-8">
						Enter the details of the new blood unit to be added to the inventory.
					</p>

					<form @submit.prevent="handleSubmit" class="space-y-8">
						<!-- Main Form Grid -->
						<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
							<!-- Left Column -->
							<div class="space-y-6">
								<!-- Anonymous Donor Checkbox -->
								<div class="flex items-start">
									<div class="flex items-center h-5">
										<input
											id="anonymous-donor"
											type="checkbox"
											v-model="anonymousDonor"
											class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"
										/>
									</div>
									<div class="ml-3">
										<label
											for="anonymous-donor"
											class="text-sm font-medium text-gray-700"
										>
											Anonymous Donor
										</label>
									</div>
								</div>

								<!-- Donor ID -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Donor ID</label
									>
									<input
										type="text"
										v-model="donorId"
										:disabled="anonymousDonor"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:cursor-not-allowed"
										placeholder="Enter donor ID"
									/>
									<p class="text-xs text-gray-500 mt-1">
										Enter the unique ID of the donor.
									</p>
								</div>

								<!-- Donor Name -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Donor Name</label
									>
									<input
										type="text"
										v-model="donorName"
										:disabled="anonymousDonor"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:cursor-not-allowed"
										placeholder="Enter donor name"
									/>
								</div>

								<!-- Blood Group -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Blood Group</label
									>
									<select
										v-model="bloodGroup"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									>
										<option value="">Select blood group</option>
										<option value="A+">A+</option>
										<option value="A-">A-</option>
										<option value="B+">B+</option>
										<option value="B-">B-</option>
										<option value="AB+">AB+</option>
										<option value="AB-">AB-</option>
										<option value="O+">O+</option>
										<option value="O-">O-</option>
									</select>
								</div>

								<!-- Quantity -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Quantity (units)</label
									>
									<input
										type="number"
										v-model="quantity"
										min="1"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
										placeholder="1"
									/>
									<p class="text-xs text-gray-500 mt-1">
										Standard unit is 450ml of whole blood.
									</p>
								</div>
							</div>

							<!-- Right Column -->
							<div class="space-y-6">
								<!-- Collection Date -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Collection Date</label
									>
									<div class="relative">
										<input
											type="date"
											v-model="collectionDate"
											class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
										/>
									</div>
								</div>

								<!-- Expiry Date -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Expiry Date</label
									>
									<div class="relative">
										<input
											type="date"
											v-model="expiryDate"
											:min="minExpiryDate"
											class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
										/>
									</div>
									<p class="text-xs text-gray-500 mt-1">
										Typically 35-42 days after collection for whole blood.
									</p>
								</div>

								<!-- Source Type -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Source Type</label
									>
									<select
										v-model="sourceType"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									>
										<option value="">Select source type</option>
										<option value="voluntary">Voluntary Donation</option>
										<option value="replacement">Replacement Donation</option>
										<option value="autologous">Autologous Donation</option>
										<option value="directed">Directed Donation</option>
										<option value="apheresis">Apheresis</option>
									</select>
								</div>

								<!-- Collection Location -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Collection Location</label
									>
									<input
										type="text"
										v-model="collectionLocation"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
										placeholder="Enter collection location"
									/>
								</div>
							</div>
						</div>

						<!-- Processing Status -->
						<div
							class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-6 border-t border-gray-200"
						>
							<!-- Screening Complete -->
							<div class="p-4 bg-gray-50 rounded-lg">
								<div class="flex items-start">
									<div class="flex items-center h-5">
										<input
											id="screening-complete"
											type="checkbox"
											v-model="screeningComplete"
											class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"
										/>
									</div>
									<div class="ml-3">
										<label
											for="screening-complete"
											class="text-sm font-medium text-gray-700"
										>
											Screening Complete
										</label>
										<p class="text-xs text-gray-500 mt-1">
											Blood has been screened for infectious diseases.
										</p>
									</div>
								</div>
							</div>

							<!-- Processing Complete -->
							<div class="p-4 bg-gray-50 rounded-lg">
								<div class="flex items-start">
									<div class="flex items-center h-5">
										<input
											id="processing-complete"
											type="checkbox"
											v-model="processingComplete"
											class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"
										/>
									</div>
									<div class="ml-3">
										<label
											for="processing-complete"
											class="text-sm font-medium text-gray-700"
										>
											Processing Complete
										</label>
										<p class="text-xs text-gray-500 mt-1">
											Blood has been processed and is ready for storage.
										</p>
									</div>
								</div>
							</div>
						</div>

						<!-- Additional Notes -->
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Additional Notes</label
							>
							<textarea
								v-model="additionalNotes"
								rows="4"
								class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
								placeholder="Enter any additional information about this blood unit"
							></textarea>
						</div>

						<!-- Form Actions -->
						<div class="flex justify-end pt-6 border-t border-gray-200">
							<button
								type="submit"
								class="px-6 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gray-900 hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900 transition-colors"
							>
								Add Blood Unit
							</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

// Form data
const anonymousDonor = ref(false)
const donorId = ref('')
const donorName = ref('')
const bloodGroup = ref('')
const quantity = ref(1)
const collectionDate = ref(new Date().toISOString().split('T')[0])
const expiryDate = ref('')
const sourceType = ref('')
const collectionLocation = ref('')
const screeningComplete = ref(false)
const processingComplete = ref(false)
const additionalNotes = ref('')

// Computed properties
const minExpiryDate = computed(() => {
	if (collectionDate.value) {
		const date = new Date(collectionDate.value)
		date.setDate(date.getDate() + 1) // Minimum 1 day after collection
		return date.toISOString().split('T')[0]
	}
	return ''
})

// Watchers
watch(anonymousDonor, (newValue) => {
	if (newValue) {
		donorId.value = ''
		donorName.value = ''
	}
})

watch(collectionDate, (newDate) => {
	if (newDate && !expiryDate.value) {
		// Auto-calculate expiry date (35 days after collection for whole blood)
		const date = new Date(newDate)
		date.setDate(date.getDate() + 35)
		expiryDate.value = date.toISOString().split('T')[0]
	}
})

// Form handlers
const handleSubmit = () => {
	// Validate required fields
	const requiredFields = [
		{ field: bloodGroup.value, name: 'Blood Group' },
		{ field: quantity.value, name: 'Quantity' },
		{ field: collectionDate.value, name: 'Collection Date' },
		{ field: expiryDate.value, name: 'Expiry Date' },
		{ field: sourceType.value, name: 'Source Type' },
		{ field: collectionLocation.value, name: 'Collection Location' },
	]

	if (!anonymousDonor.value) {
		requiredFields.push(
			{ field: donorId.value, name: 'Donor ID' },
			{ field: donorName.value, name: 'Donor Name' },
		)
	}

	const missingFields = requiredFields.filter((item) => !item.field).map((item) => item.name)

	if (missingFields.length > 0) {
		alert(`Please fill in the following required fields: ${missingFields.join(', ')}`)
		return
	}

	// Validate expiry date is after collection date
	if (new Date(expiryDate.value) <= new Date(collectionDate.value)) {
		alert('Expiry date must be after collection date')
		return
	}

	// Collect form data
	const formData = {
		anonymousDonor: anonymousDonor.value,
		donorId: anonymousDonor.value ? null : donorId.value,
		donorName: anonymousDonor.value ? null : donorName.value,
		bloodGroup: bloodGroup.value,
		quantity: quantity.value,
		collectionDate: collectionDate.value,
		expiryDate: expiryDate.value,
		sourceType: sourceType.value,
		collectionLocation: collectionLocation.value,
		screeningComplete: screeningComplete.value,
		processingComplete: processingComplete.value,
		additionalNotes: additionalNotes.value,
	}

	console.log('Blood unit added:', formData)
	alert('Blood unit added successfully!')
}

const handleCancel = () => {
	if (confirm('Are you sure you want to cancel? All unsaved changes will be lost.')) {
		// Reset form data
		anonymousDonor.value = false
		donorId.value = ''
		donorName.value = ''
		bloodGroup.value = ''
		quantity.value = 1
		collectionDate.value = new Date().toISOString().split('T')[0]
		expiryDate.value = ''
		sourceType.value = ''
		collectionLocation.value = ''
		screeningComplete.value = false
		processingComplete.value = false
		additionalNotes.value = ''
	}
}
</script>
