<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Navigation Tabs -->
		<div class="mb-6">
			<nav class="flex space-x-8 border-b border-gray-200">
				<button
					v-for="tab in tabs"
					:key="tab.name"
					@click="activeTab = tab.name"
					:class="[
						'py-2 px-1 border-b-2 font-medium text-sm',
						activeTab === tab.name
							? 'border-blue-500 text-blue-600'
							: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
					]"
				>
					{{ tab.label }}
				</button>
			</nav>
		</div>

		<!-- Form Content -->
		<div class="bg-white rounded-lg shadow-sm border border-gray-200">
			<form @submit.prevent="handleSubmit" class="p-6 md:p-8">
				<!-- Basic Information Section -->
				<div class="mb-8">
					<h2 class="text-xl font-semibold text-gray-900 mb-2">Basic Information</h2>
					<p class="text-sm text-gray-600 mb-6">
						Enter the basic details of the inventory item
					</p>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<!-- Item Name -->
						<div>
							<label
								for="itemName"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Item Name
							</label>
							<input
								id="itemName"
								v-model="formData.itemName"
								type="text"
								placeholder="Enter item name"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
						</div>

						<!-- Item ID/SKU -->
						<div>
							<label
								for="itemSku"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Item ID/SKU
							</label>
							<input
								id="itemSku"
								v-model="formData.itemSku"
								type="text"
								placeholder="Enter item ID or SKU"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
						</div>

						<!-- Category -->
						<div>
							<label
								for="category"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Category
							</label>
							<select
								id="category"
								v-model="formData.category"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							>
								<option value="">Select category</option>
								<option value="Medical Supplies">Medical Supplies</option>
								<option value="Medications">Medications</option>
								<option value="Equipment">Equipment</option>
								<option value="Consumables">Consumables</option>
							</select>
						</div>

						<!-- Subcategory -->
						<div>
							<label
								for="subcategory"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Subcategory
							</label>
							<select
								id="subcategory"
								v-model="formData.subcategory"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
								:disabled="!formData.category"
							>
								<option value="">Select subcategory</option>
								<option
									v-for="subcat in availableSubcategories"
									:key="subcat"
									:value="subcat"
								>
									{{ subcat }}
								</option>
							</select>
						</div>

						<!-- Description (Full Width) -->
						<div class="md:col-span-2">
							<label
								for="description"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Description
							</label>
							<textarea
								id="description"
								v-model="formData.description"
								rows="4"
								placeholder="Enter item description"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-none"
							></textarea>
						</div>

						<!-- Unit of Measure -->
						<div>
							<label
								for="unitOfMeasure"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Unit of Measure
							</label>
							<select
								id="unitOfMeasure"
								v-model="formData.unitOfMeasure"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							>
								<option value="">Select unit</option>
								<option value="pieces">Pieces</option>
								<option value="boxes">Boxes</option>
								<option value="bottles">Bottles</option>
								<option value="vials">Vials</option>
								<option value="packs">Packs</option>
								<option value="units">Units</option>
							</select>
						</div>

						<!-- Unit Quantity -->
						<div>
							<label
								for="unitQuantity"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Unit Quantity
							</label>
							<input
								id="unitQuantity"
								v-model="formData.unitQuantity"
								type="number"
								placeholder="Quantity per unit"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
						</div>

						<!-- Storage Location -->
						<div>
							<label
								for="storageLocation"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Storage Location
							</label>
							<input
								id="storageLocation"
								v-model="formData.storageLocation"
								type="text"
								placeholder="Enter storage location"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
						</div>
					</div>
				</div>

				<!-- Additional Information Section -->
				<div class="mb-8">
					<h2 class="text-xl font-semibold text-gray-900 mb-2">
						Additional Information
					</h2>
					<p class="text-sm text-gray-600 mb-6">
						Enter additional details about the item
					</p>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<!-- Manufacturer -->
						<div>
							<label
								for="manufacturer"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Manufacturer
							</label>
							<input
								id="manufacturer"
								v-model="formData.manufacturer"
								type="text"
								placeholder="Enter manufacturer"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
						</div>

						<!-- Brand -->
						<div>
							<label
								for="brand"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Brand
							</label>
							<input
								id="brand"
								v-model="formData.brand"
								type="text"
								placeholder="Enter brand name"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
						</div>

						<!-- Model/Version -->
						<div>
							<label
								for="modelVersion"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Model/Version
							</label>
							<input
								id="modelVersion"
								v-model="formData.modelVersion"
								type="text"
								placeholder="Enter model or version"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
						</div>

						<!-- Expiry Tracking -->
						<div>
							<label
								for="expiryTracking"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Expiry Tracking
							</label>
							<select
								id="expiryTracking"
								v-model="formData.expiryTracking"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							>
								<option value="">Select option</option>
								<option value="enabled">Enabled</option>
								<option value="disabled">Disabled</option>
								<option value="manual">Manual Tracking</option>
							</select>
						</div>
					</div>

					<!-- Item Properties -->
					<div class="mt-6">
						<label class="block text-sm font-medium text-gray-700 mb-3">
							Item Properties
						</label>
						<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
							<div class="space-y-3">
								<label class="flex items-center">
									<input
										v-model="formData.requiresRefrigeration"
										type="checkbox"
										class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
									/>
									<span class="ml-2 text-sm text-gray-700"
										>Requires Refrigeration</span
									>
								</label>
								<label class="flex items-center">
									<input
										v-model="formData.hazardousMaterial"
										type="checkbox"
										class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
									/>
									<span class="ml-2 text-sm text-gray-700"
										>Hazardous Material</span
									>
								</label>
							</div>
							<div class="space-y-3">
								<label class="flex items-center">
									<input
										v-model="formData.controlledSubstance"
										type="checkbox"
										class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
									/>
									<span class="ml-2 text-sm text-gray-700"
										>Controlled Substance</span
									>
								</label>
								<label class="flex items-center">
									<input
										v-model="formData.sterile"
										type="checkbox"
										class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
									/>
									<span class="ml-2 text-sm text-gray-700">Sterile</span>
								</label>
							</div>
						</div>
					</div>

					<!-- Notes -->
					<div class="mt-6">
						<label for="notes" class="block text-sm font-medium text-gray-700 mb-2">
							Notes
						</label>
						<textarea
							id="notes"
							v-model="formData.notes"
							rows="4"
							placeholder="Enter any additional notes"
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-none"
						></textarea>
					</div>
				</div>

				<!-- Action Buttons -->
				<div class="flex flex-col sm:flex-row gap-3 sm:justify-end">
					<button
						type="button"
						@click="handleCancel"
						class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
					>
						Cancel
					</button>
					<button
						type="submit"
						class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 flex items-center gap-2"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M5 13l4 4L19 7"
							></path>
						</svg>
						Save Item
					</button>
				</div>
			</form>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Navigation tabs
const tabs = [
	{ name: 'details', label: 'Item Details' },
	{ name: 'stock', label: 'Stock Management' },
	{ name: 'suppliers', label: 'Suppliers' },
]

const activeTab = ref('details')

// Form data
const formData = ref({
	itemName: '',
	itemSku: '',
	category: '',
	subcategory: '',
	description: '',
	unitOfMeasure: '',
	unitQuantity: '',
	storageLocation: '',
	manufacturer: '',
	brand: '',
	modelVersion: '',
	expiryTracking: '',
	requiresRefrigeration: false,
	hazardousMaterial: false,
	controlledSubstance: false,
	sterile: false,
	notes: '',
})

// Subcategories based on selected category
const subcategories = {
	'Medical Supplies': ['Disposables', 'Instruments', 'Safety Equipment', 'Wound Care'],
	Medications: ['Prescription', 'Over-the-Counter', 'Controlled Substances', 'Vaccines'],
	Equipment: ['Diagnostic', 'Monitoring', 'Surgical', 'Laboratory'],
	Consumables: ['Office Supplies', 'Cleaning', 'Maintenance', 'Packaging'],
}

const availableSubcategories = computed(() => {
	return formData.value.category ? subcategories[formData.value.category] || [] : []
})

// Form handlers
const handleSubmit = () => {
	console.log('Form submitted:', formData.value)
	// Handle form submission logic here
}

const handleCancel = () => {
	// Reset form or navigate back
	console.log('Form cancelled')
}

// Watch for category changes to reset subcategory
import { watch } from 'vue'
watch(
	() => formData.value.category,
	() => {
		formData.value.subcategory = ''
	},
)
</script>
