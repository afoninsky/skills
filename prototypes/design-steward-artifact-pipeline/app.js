/*
 * THROWAWAY PROTOTYPE.
 * Three structurally different rescheduling views, switchable with ?variant=A|B|C.
 * The same scenario data and in-memory state are rendered by every variant.
 */

const variants = [
  { key: "A", name: "Workbench board" },
  { key: "B", name: "Guided route" },
  { key: "C", name: "Parts ledger" },
];

const sessions = [
  {
    id: "tue-1830",
    day: "Tue",
    date: "12 Aug",
    time: "18:30–20:00",
    place: "Workshop hall",
    repairers: "Mara + Jules",
    availability: "2 places left",
    access: "Step-free · induction loop",
    fit: "Best match",
    available: true,
  },
  {
    id: "sat-1000",
    day: "Sat",
    date: "16 Aug",
    time: "10:00–11:30",
    place: "Quiet bench",
    repairers: "Jules",
    availability: "1 place left",
    access: "Step-free · low-sensory session",
    fit: "Quieter",
    available: true,
  },
  {
    id: "mon-1900",
    day: "Mon",
    date: "18 Aug",
    time: "19:00–20:30",
    place: "Workshop hall",
    repairers: "Mara + Ivo",
    availability: "4 places left",
    access: "Step-free · induction loop",
    fit: "More room",
    available: true,
  },
  {
    id: "wed-1730",
    day: "Wed",
    date: "20 Aug",
    time: "17:30–19:00",
    place: "Workshop hall",
    repairers: "Ivo",
    availability: "Full",
    access: "Step-free",
    fit: "Waitlist only",
    available: false,
  },
];

const state = {
  bookingId: "CR-0842",
  item: "Table lamp",
  currentSession: "Thu 14 Aug · 19:00–20:30",
  selectedSessionId: null,
  confirmed: false,
  showAlternatives: false,
  validationMessage: "",
};

const root = document.querySelector("#prototype-root");
const announcer = document.querySelector("#prototype-announcer");
const variantLabel = document.querySelector("#variant-label");

function currentVariant() {
  const requested = new URLSearchParams(window.location.search).get("variant")?.toUpperCase();
  return variants.find((variant) => variant.key === requested) ?? variants[0];
}

function selectedSession() {
  return sessions.find((session) => session.id === state.selectedSessionId) ?? null;
}

function ticketMarkup() {
  return `
    <aside class="repair-ticket" aria-label="Current booking">
      <div class="ticket-notches" aria-hidden="true"></div>
      <p class="ticket-label">Current repair ticket</p>
      <p class="ticket-number">${state.bookingId}</p>
      <h2>${state.item}</h2>
      <dl>
        <div><dt>Booked</dt><dd>${state.currentSession}</dd></div>
        <div><dt>Place</dt><dd>Workshop hall</dd></div>
        <div><dt>Change fee</dt><dd>None</dd></div>
      </dl>
      <p class="ticket-note">Your item notes and photos move with the booking.</p>
    </aside>`;
}

function statusMarkup() {
  const chosen = selectedSession();
  const summary = {
    bookingId: state.bookingId,
    item: state.item,
    currentSession: state.currentSession,
    selectedSession: chosen
      ? `${chosen.day} ${chosen.date} · ${chosen.time} · ${chosen.place}`
      : null,
    confirmedInPrototype: state.confirmed,
    persistence: "none — in-memory prototype",
  };

  return `
    <details class="state-ledger" open>
      <summary>Visible prototype state</summary>
      <pre>${JSON.stringify(summary, null, 2)}</pre>
    </details>`;
}

function validationMarkup() {
  if (!state.validationMessage) return "";
  return `<p class="validation-message" role="alert">${state.validationMessage}</p>`;
}

function confirmMarkup(buttonLabel = "Confirm new time") {
  const chosen = selectedSession();
  if (state.confirmed && chosen) {
    return `
      <section class="confirmation" tabindex="-1">
        <p class="artifact-kicker">Prototype outcome</p>
        <h2>New time held in memory</h2>
        <p><strong>${chosen.day} ${chosen.date}, ${chosen.time}</strong> at ${chosen.place}.</p>
        <p>No booking was changed. This prototype has no backend or persistence.</p>
        <button class="secondary-action" type="button" data-action="reset">Try another time</button>
      </section>`;
  }

  return `
    <div class="confirm-actions">
      ${validationMarkup()}
      <button class="primary-action" type="button" data-action="confirm">${buttonLabel}</button>
      <p>No payment or booking change occurs in this prototype.</p>
    </div>`;
}

function VariantA() {
  const cards = sessions
    .map(
      (session) => `
        <button
          class="bench-slot ${state.selectedSessionId === session.id ? "is-selected" : ""}"
          type="button"
          data-session-id="${session.id}"
          ${session.available ? "" : "disabled"}
          aria-pressed="${state.selectedSessionId === session.id}"
        >
          <span class="slot-fit">${session.fit}</span>
          <span class="slot-day">${session.day}</span>
          <span class="slot-date">${session.date}</span>
          <span class="slot-time">${session.time}</span>
          <span class="slot-place">${session.place}</span>
          <span class="slot-meta">${session.repairers}</span>
          <span class="slot-meta">${session.access}</span>
          <span class="slot-availability">${session.availability}</span>
        </button>`,
    )
    .join("");

  return `
    <article class="variant variant-a">
      <section class="board-hero">
        <div class="board-intro">
          <p class="artifact-kicker">Direction A · spatial comparison</p>
          <h1>Move your lamp to another workbench.</h1>
          <p class="lede">All compatible electrical-repair sessions are on the board. Compare access, repairers, and remaining room before choosing.</p>
          <ol class="mini-process" aria-label="Rescheduling progress">
            <li class="is-done">Booking found</li>
            <li class="is-current">Choose a bench</li>
            <li>Check and confirm</li>
          </ol>
        </div>
        ${ticketMarkup()}
      </section>

      <section class="workbench" aria-labelledby="available-benches">
        <div class="section-heading">
          <div>
            <p class="artifact-kicker">Electrical repair · next 10 days</p>
            <h2 id="available-benches">Available benches</h2>
          </div>
          <p class="tool-note">Select one ticket-shaped slot</p>
        </div>
        <div class="bench-grid">${cards}</div>
      </section>

      ${confirmMarkup("Hold this workbench")}
      ${statusMarkup()}
    </article>`;
}

function VariantB() {
  const recommended = sessions[0];
  const alternatives = sessions.slice(1);

  return `
    <article class="variant variant-b">
      <aside class="route-rail" aria-label="Rescheduling steps">
        <p class="rail-mark">REPAIR / ROUTE</p>
        <ol>
          <li class="is-done"><span>1</span> Booking</li>
          <li class="is-current"><span>2</span> New time</li>
          <li><span>3</span> Check</li>
        </ol>
        <p class="rail-help"><strong>Need a different repair type?</strong><br />Return to your booking before choosing a time.</p>
      </aside>

      <div class="route-main">
        <header class="route-heading">
          <p class="artifact-kicker">Direction B · guided decision</p>
          <h1>Choose the next workable time.</h1>
          <p>We matched your table lamp with electrical repairers and carried over your notes.</p>
        </header>

        <section class="route-current">
          <p class="route-label">Changing</p>
          <p><strong>${state.currentSession}</strong></p>
          <span>Booking ${state.bookingId} · ${state.item}</span>
        </section>

        <section class="recommended-slot" aria-labelledby="recommended-heading">
          <div>
            <p class="route-label">Earliest strong match</p>
            <h2 id="recommended-heading">${recommended.day} ${recommended.date}</h2>
            <p class="route-time">${recommended.time}</p>
          </div>
          <dl>
            <div><dt>Repairers</dt><dd>${recommended.repairers}</dd></div>
            <div><dt>Access</dt><dd>${recommended.access}</dd></div>
            <div><dt>Room</dt><dd>${recommended.availability}</dd></div>
          </dl>
          <button
            class="primary-action"
            type="button"
            data-session-id="${recommended.id}"
            aria-pressed="${state.selectedSessionId === recommended.id}"
          >${state.selectedSessionId === recommended.id ? "Selected" : "Choose this time"}</button>
        </section>

        <button class="text-action" type="button" data-action="show-alternatives" aria-expanded="${state.showAlternatives}">
          ${state.showAlternatives ? "Hide other compatible times" : "Show three other compatible times"}
        </button>

        ${
          state.showAlternatives
            ? `<div class="route-alternatives">${alternatives
                .map(
                  (session) => `
                    <button
                      type="button"
                      class="route-option ${state.selectedSessionId === session.id ? "is-selected" : ""}"
                      data-session-id="${session.id}"
                      ${session.available ? "" : "disabled"}
                      aria-pressed="${state.selectedSessionId === session.id}"
                    >
                      <span><strong>${session.day} ${session.date}</strong><small>${session.time}</small></span>
                      <span><strong>${session.fit}</strong><small>${session.access}</small></span>
                      <span>${session.availability}</span>
                    </button>`,
                )
                .join("")}</div>`
            : ""
        }

        ${confirmMarkup("Continue to check")}
        ${statusMarkup()}
      </div>
    </article>`;
}

function VariantC() {
  const rows = sessions
    .map(
      (session) => `
        <tr class="${state.selectedSessionId === session.id ? "is-selected" : ""}">
          <td>
            <input
              id="ledger-${session.id}"
              type="radio"
              name="ledger-session"
              value="${session.id}"
              data-session-id="${session.id}"
              ${state.selectedSessionId === session.id ? "checked" : ""}
              ${session.available ? "" : "disabled"}
            />
          </td>
          <th scope="row"><label for="ledger-${session.id}">${session.day} ${session.date}<small>${session.time}</small></label></th>
          <td>${session.place}<small>${session.repairers}</small></td>
          <td>${session.access}</td>
          <td><span class="ledger-status ${session.available ? "" : "is-full"}">${session.availability}</span></td>
          <td>${session.fit}</td>
        </tr>`,
    )
    .join("");

  return `
    <article class="variant variant-c">
      <header class="ledger-heading">
        <div>
          <p class="artifact-kicker">Direction C · dense comparison</p>
          <h1>Rescheduling ledger</h1>
        </div>
        <div class="ledger-booking">
          <span>Booking</span>
          <strong>${state.bookingId}</strong>
          <span>${state.item}</span>
        </div>
      </header>

      <section class="ledger-notice" aria-label="Current booking">
        <p><span>Current</span><strong>${state.currentSession}</strong></p>
        <p><span>Carried forward</span><strong>Item notes · photos · electrical category</strong></p>
      </section>

      <section class="ledger-panel" aria-labelledby="ledger-options">
        <div class="ledger-toolbar">
          <div>
            <p class="artifact-kicker">Compatible inventory</p>
            <h2 id="ledger-options">Compare every field</h2>
          </div>
          <p>4 sessions · 3 available</p>
        </div>
        <div class="table-scroll" tabindex="0" aria-label="Scrollable session comparison">
          <table>
            <thead>
              <tr>
                <th><span class="visually-hidden">Choose</span></th>
                <th>Date</th>
                <th>Place / repairers</th>
                <th>Access</th>
                <th>Room</th>
                <th>Fit</th>
              </tr>
            </thead>
            <tbody>${rows}</tbody>
          </table>
        </div>
      </section>

      <div class="ledger-footer">
        <div>
          <p class="route-label">Selection</p>
          <p>${selectedSession() ? `${selectedSession().day} ${selectedSession().date} · ${selectedSession().time}` : "No replacement time selected"}</p>
        </div>
        ${confirmMarkup("Review selected time")}
      </div>
      ${statusMarkup()}
    </article>`;
}

function render() {
  const variant = currentVariant();
  const renderer = { A: VariantA, B: VariantB, C: VariantC }[variant.key];
  root.innerHTML = renderer();
  variantLabel.textContent = `${variant.key} — ${variant.name}`;
  document.title = `${variant.key} — ${variant.name} · Repair session prototype`;
  bindVariantActions();
}

function chooseSession(sessionId) {
  const session = sessions.find((candidate) => candidate.id === sessionId);
  if (!session?.available) return;
  state.selectedSessionId = session.id;
  state.confirmed = false;
  state.validationMessage = "";
  render();
  announcer.textContent = `Selected ${session.day} ${session.date}, ${session.time}.`;
}

function bindVariantActions() {
  document.querySelectorAll("[data-session-id]").forEach((control) => {
    const eventName = control.matches('input[type="radio"]') ? "change" : "click";
    control.addEventListener(eventName, (event) => chooseSession(event.currentTarget.dataset.sessionId));
  });

  document.querySelectorAll('[data-action="confirm"]').forEach((control) => {
    control.addEventListener("click", () => {
      if (!selectedSession()) {
        state.validationMessage = "Choose an available replacement time before continuing.";
      } else {
        state.validationMessage = "";
        state.confirmed = true;
      }
      render();
      const confirmation = document.querySelector(".confirmation");
      confirmation?.focus();
    });
  });

  document.querySelectorAll('[data-action="reset"]').forEach((control) => {
    control.addEventListener("click", () => {
      state.selectedSessionId = null;
      state.confirmed = false;
      state.validationMessage = "";
      render();
    });
  });

  document.querySelectorAll('[data-action="show-alternatives"]').forEach((control) => {
    control.addEventListener("click", () => {
      state.showAlternatives = !state.showAlternatives;
      render();
    });
  });
}

function cycleVariant(offset) {
  const active = currentVariant();
  const index = variants.findIndex((variant) => variant.key === active.key);
  const next = variants[(index + offset + variants.length) % variants.length];
  const url = new URL(window.location.href);
  url.searchParams.set("variant", next.key);
  history.replaceState({}, "", url);
  state.validationMessage = "";
  render();
  announcer.textContent = `Showing ${next.key}, ${next.name}.`;
}

document.querySelector("#previous-variant").addEventListener("click", () => cycleVariant(-1));
document.querySelector("#next-variant").addEventListener("click", () => cycleVariant(1));
window.addEventListener("popstate", render);
window.addEventListener("keydown", (event) => {
  const target = event.target;
  const isEditing = target.matches("input, textarea, select, button, [contenteditable]");
  if (isEditing) return;
  if (event.key === "ArrowLeft") cycleVariant(-1);
  if (event.key === "ArrowRight") cycleVariant(1);
});

render();
